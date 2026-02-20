import os
from dotenv import load_dotenv
from groq import Groq

from src.extract_pdf import extract_text
from src.splitter import split_into_passages

# Load Groq API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"   # 🔥 NEW WORKING MODEL

class PDFEngine:
    def __init__(self):
        self.passages = None
        self.summary = None

    def load_pdf(self, pdf_path):
        text_path = "./data/extracted.txt"

        # Extract the PDF text
        extract_text(pdf_path, text_path)

        with open(text_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Ask Groq to summarize and enforce structured markdown output
        summary_prompt = f"""
Summarize this PDF clearly and briefly. RETURN ONLY MARKDOWN in the exact structure below (no extra text):

## Overview
- (3-6 concise bullet points summarizing main ideas)

## Key Concepts
- (bullet points of key terms; use **bold** for important terms)

## Conclusion
- (1-2 concise concluding points)

Keep bullets short and use simple sentences. Now summarize the PDF text below.

PDF TEXT:
{text}
"""

        summary_resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": summary_prompt}]
        )

        self.summary = summary_resp.choices[0].message.content

        # Split into passages
        self.passages = split_into_passages(text)

        return {
            "summary": self.summary,
            "total_passages": len(self.passages)
        }

    def get_auto_questions(self):
        if not self.passages:
            return []

        prompt = f"Generate 5 helpful questions based on this text:\n\n{self.passages[0]}"

        resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return resp.choices[0].message.content.split("\n")

    def ask(self, user_q):
        full_text = "\n\n".join(self.passages)

        # Instruct model to produce a structured markdown answer
        prompt = (
            "You are given a user's question and the PDF content. "
            "Answer using ONLY the provided PDF text. RETURN ONLY MARKDOWN in the exact format below (no extra commentary):\n\n"
            "**Short explanation**\n"
            "- (2-4 concise bullet points; bold key terms using **bold**)\n\n"
            "**Final insight**\n"
            "- (one-line final insight)\n\n"
            f"Question: {user_q}\n\n"
            f"PDF Content:\n{full_text}"
        )

        resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        answer = resp.choices[0].message.content

        return {
            "answer": answer,
            "passage": "Groq LLM used for reasoning over the full PDF"
        }