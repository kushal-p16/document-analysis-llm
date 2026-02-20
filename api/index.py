from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tempfile
import sys
import os

# Add parent directory to path to import backend
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend import PDFEngine

app = FastAPI()
engine = PDFEngine()

# CORS configuration for Vercel deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:8080",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
        "https://*.vercel.app",  # Allow all Vercel deployments
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schema for /ask endpoint
class AskRequest(BaseModel):
    question: str
    passages: list[str]


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Save PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            pdf_path = tmp.name

        # Process PDF with Groq
        result = engine.load_pdf(pdf_path)

        return {
            "status": "success",
            "summary": result["summary"],
            "keywords": result.get("keywords", []),
            "passages": engine.passages,
        }

    except Exception as e:
        print("UPLOAD ERROR:", e)
        return {"status": "error", "message": str(e)}


@app.post("/ask")
async def ask_question(payload: AskRequest):
    try:
        engine.passages = payload.passages
        llm_result = engine.ask(payload.question)

        return {
            "status": "success",
            "answer": llm_result["answer"],
        }

    except Exception as e:
        print("ASK ERROR:", e)
        return {"status": "error", "message": str(e)}
