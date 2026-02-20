# ⭐ AI PDF Analyst

A full-stack intelligent document analysis system built using FastAPI, React, Groq LLMs, and advanced NLP pipelines.
Upload any PDF → get instant summaries, keywords, and ask questions freely.

## 🚀 Features

- 📄 Upload any PDF
- 🔍 Automatic text extraction
- 🧠 AI-powered Summary (Groq LLaMA 3.1 8B Instant)
- 🔑 Keyword extraction
- ❓ Ask questions about the PDF
- ⚡ Fast, beautiful modern UI (React + Vite + Shadcn UI)
- 🔥 FastAPI backend with clean REST endpoints
- 🔐 Supports local development (no deployment required)

## 🏗 Tech Stack

### Frontend

- React + Vite
- TypeScript
- Shadcn/UI
- Tailwind CSS
- React Query
- Lucide Icons

### Backend

- FastAPI
- Python 3.10
- GROQ LLMs
- PyPDF2 for PDF extraction

## 📁 Project Structure

```
document-analysis-llm/
│
├── backend.py
├── fastapi_server.py
├── app.py (Streamlit old version)
├── src/
│   ├── extract_pdf.py
│   ├── splitter.py
│   ├── summarizer.py
│   ├── rag_engine.py
│   ├── question_generator.py
│   ├── ...
│
├── ui-react/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Index.tsx
│   │   │   ├── NotFound.tsx
│   │   ├── components/
│   │   │   ├── UploadZone.tsx
│   │   │   ├── ResultsPanel.tsx
│   │   │   ├── LoadingSpinner.tsx
│   ├── public/
│   ├── package.json
│
├── data/
│   ├── extracted.txt
+  ├── yourpdf.pdf
│
└── README.md
```

## 🛠 Installation & Setup

1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/document-analysis-llm.git
cd document-analysis-llm
```

### 🖥 Backend Setup (FastAPI + Groq)

2️⃣ Create virtual environment

```bash
python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Add your GROQ API key

Create a `.env` file at the project root with:

```text
GROQ_API_KEY=your_api_key_here
```

5️⃣ Run FastAPI server

```bash
uvicorn fastapi_server:app --reload
```

Backend will start at:

👉 http://127.0.0.1:8000

### 🌐 Frontend Setup (React + Vite)

6️⃣ Go to UI folder

```bash
cd ui-react
npm install
npm run dev
```

Frontend will start at (Vite default):

👉 http://localhost:5173 (or the port displayed by Vite)

## 🔌 API Endpoints

### POST /upload

Upload a PDF and get summary + keywords + passages.

Response:

```json
{
  "status": "success",
  "summary": "...",
  "keywords": ["...", "..."],
  "passages": ["..."]
}
```

### POST /ask

Ask a question about the uploaded PDF.

Request:

```json
{
  "question": "What is the topic?",
  "passages": [ ... ]
}
```

Response:

```json
{
  "status": "success",
  "answer": "..."
}
```

## � Deployment

### ⚠️ Why NOT Vercel?

Vercel was initially attempted but encountered issues:
- **Module Resolution:** Vercel's build system struggles with resolving relative paths in Vite projects with complex configurations
- **Configuration Complexity:** Vercel requires specific `vercel.json` setups that conflicted with the dual-deployment architecture (frontend + Railway backend)
- **Build Inconsistencies:** Multiple configuration attempts resulted in repeated build failures

### ✅ Deployed on Netlify

**Frontend:** Deployed on [Netlify](https://netlify.com) with automatic builds from GitHub.

**Backend:** Running on [Railway](https://railway.app) as a Docker container (see `Dockerfile` and `railway.json`).

**Configuration:**
- Frontend automatically builds from `ui-react/` directory
- Netlify redirects all routes to `index.html` for React routing
- Environment variables in Netlify:
  - `VITE_API_URL`: Points to Railway backend at `https://document-analysis-llm-production.up.railway.app`

**To Deploy:**
1. Push code to GitHub
2. Connect your GitHub repo to Netlify
3. Set Root Directory to `ui-react`
4. Build Command: `npm install && npm run build`
5. Publish Directory: `dist`
6. Add environment variable: `VITE_API_URL=https://document-analysis-llm-production.up.railway.app`
7. Deploy!

See `netlify.toml` for automated configuration.

## �🖼 Screenshots (Add later)

/screenshots/home.png
/screenshots/upload.png
/screenshots/results.png

## ✔ Future Enhancements

- Add user authentication
- Add PDF highlighting
- Provide downloadable summaries
- Convert results to DOCX/PDF
- Support multiple files
- Database for saved documents
- Advanced analytics dashboard

## ⭐ Credits

Built by Kushal P – AI/ML Engineer in progress 🚀
Guided & Co-developed with ChatGPT

## 📜 License

MIT License – free to use & modify.
