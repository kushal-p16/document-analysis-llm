from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tempfile
import sys
import os

# Add parent directory to path to import backend
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from backend import PDFEngine
except ImportError:
    # Fallback if import fails
    print("Warning: Could not import PDFEngine")
    PDFEngine = None

app = FastAPI(title="PDF Analyst API")

# Initialize engine only if import successful
if PDFEngine:
    engine = PDFEngine()
else:
    engine = None

# CORS configuration for Vercel deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schema for /ask endpoint
class AskRequest(BaseModel):
    question: str
    passages: list[str]


@app.get("/health")
async def health_check():
    """Health check endpoint for Vercel"""
    return {"status": "ok", "service": "PDF Analyst API"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """Upload and analyze PDF"""
    if not engine:
        return {"status": "error", "message": "Backend engine not initialized"}
    
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
        print(f"UPLOAD ERROR: {str(e)}")
        return {"status": "error", "message": f"Upload failed: {str(e)}"}


@app.post("/ask")
async def ask_question(payload: AskRequest):
    """Answer question about PDF"""
    if not engine:
        return {"status": "error", "message": "Backend engine not initialized"}
    
    try:
        engine.passages = payload.passages
        llm_result = engine.ask(payload.question)

        return {
            "status": "success",
            "answer": llm_result["answer"],
        }

    except Exception as e:
        print(f"ASK ERROR: {str(e)}")
        return {"status": "error", "message": f"Question failed: {str(e)}"}

