from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend import PDFEngine
import tempfile

app = FastAPI()
engine = None  # Lazy initialization

# Allow common frontend dev origins (Vite default 5173) and localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:8080",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_engine():
    """Lazy initialization of PDFEngine"""
    global engine
    if engine is None:
        engine = PDFEngine()
    return engine

# Schema for /ask endpoint
class AskRequest(BaseModel):
    question: str
    passages: list[str]


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Get or initialize engine
        pdf_engine = get_engine()
        
        # Save PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            pdf_path = tmp.name

        # Process PDF with Groq
        result = pdf_engine.load_pdf(pdf_path)

        return {
            "status": "success",
            "summary": result["summary"],
            "keywords": result.get("keywords", []),
            "passages": pdf_engine.passages,   # send passages to frontend
        }

    except Exception as e:
        print("UPLOAD ERROR:", e)
        return {"status": "error", "message": str(e)}


@app.post("/ask")
async def ask_question(payload: AskRequest):
    try:
        # Get or initialize engine
        pdf_engine = get_engine()
        
        # Set passages coming from frontend
        pdf_engine.passages = payload.passages

        llm_result = pdf_engine.ask(payload.question)

        return {
            "status": "success",
            "answer": llm_result["answer"],
        }

    except Exception as e:
        print("ASK ERROR:", e)
        return {"status": "error", "message": str(e)}