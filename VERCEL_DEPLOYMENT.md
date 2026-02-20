# 🚀 Vercel Deployment Guide

## Overview
This project is configured for **seamless Vercel deployment** with:
- ✅ React frontend (Vite) deployed to Vercel
- ✅ FastAPI backend as Vercel serverless functions
- ✅ Integrated API calls (no separate deployments needed)
- ✅ PDF upload and AI analysis working together

---

## Step-by-Step Deployment Instructions

### **1. Go to Vercel**
- Visit: https://vercel.com
- Sign in with your GitHub account (**kushal-p16**)

### **2. Create New Project**
- Click **"Add New"** → **"Project"**
- Select **"Import Git Repository"**
- Find: **`kushal-p16/document-analysis-llm`**
- Click **"Import"**

### **3. Configure Project Settings**
The settings should auto-detect:
- **Framework Preset**: Vite
- **Build Command**: `cd ui-react && npm install && npm run build`
- **Output Directory**: `ui-react/dist`
- **Install Command**: (auto)

**Click through settings** (leave defaults) → **"Deploy"**

### **4. Add Environment Variables** ⭐ **IMPORTANT**
While the deployment is building, go to **Project Settings** → **Environment Variables**

Add this variable:
```
GROQ_API_KEY = your-actual-groq-api-key
```

Save it. Vercel will automatically redeploy with the environment variable.

### **5. Wait for Build**
- Build takes **2-5 minutes**
- You'll see the deployment progress
- Once complete, you get a live URL like: `https://document-analysis-llm.vercel.app`

---

## 🎯 How It Works

### **Frontend (React/Vite)**
- Deployed at the **root** of your Vercel domain
- Accessible at: `https://your-project.vercel.app`
- All static files served from `ui-react/dist`

### **Backend (FastAPI)**
- Deployed as **serverless functions** in `/api`
- Endpoints:
  - `POST /upload` → Upload PDF and get summary + keywords
  - `POST /ask` → Ask questions about the PDF
  - `GET /health` → Health check

### **How They Connect**
- Frontend makes API calls to `/upload` and `/ask`
- Vercel rewrites these to `/api/index.py`
- Everything runs on **the same domain** (no CORS issues)

---

## ✅ Testing After Deployment

### **1. Check Backend Health**
Open in your browser:
```
https://your-project.vercel.app/health
```
Should return: `{"status": "ok", "service": "PDF Analyst API"}`

### **2. Upload a PDF**
1. Visit: `https://your-project.vercel.app`
2. Click upload zone
3. Select a PDF file
4. Wait for summary and keywords
5. Ask questions in the Q&A section

---

## 🔧 Troubleshooting

### **Build Failed: "vite: command not found"**
✅ FIXED in current setup - npm install is now in build command

### **API Calls Failing**
- Check Vercel Logs: Project → Deployments → View Build Logs
- Ensure GROQ_API_KEY is set in Environment Variables
- Check browser console for error messages

### **"Could not import PDFEngine"**
- This is a warning and fallback is in place
- Check if all Python dependencies installed
- View Vercel Function logs

### **PDF Upload Timeout**
- Vercel Serverless Functions timeout after 10 seconds (Pro plan)
- For Production: Consider Railway/Render for backend

---

## 📝 Environment Variables Needed

Set these in **Vercel Project Settings** → **Environment Variables**:

```
GROQ_API_KEY=your-groq-api-key-here
```

---

## 📊 Project Structure for Vercel

```
project/
├── vercel.json              # Vercel config
├── requirements.txt         # Python dependencies
├── backend.py              # PDF processing engine
├── api/
│   └── index.py            # FastAPI serverless function
├── ui-react/
│   ├── package.json
│   ├── src/
│   │   ├── pages/Index.tsx       # Main app (uses /upload)
│   │   └── components/
│   │       └── ResultsPanel.tsx  # Q&A panel (uses /ask)
│   └── dist/               # Built frontend (deployed to root)
└── src/
    ├── extract_pdf.py
    ├── ner.py
    ├── etc...
```

---

## 🎉 Success!

Once deployed:
- Open `https://your-project.vercel.app`
- Upload a PDF
- Get instant summary + keywords
- Ask AI questions about the PDF
- **All on Vercel, no backend server needed!**

---

## 🆘 Need Help?

Check the:
1. **Vercel Logs** → Deployments → Most recent build
2. **Browser Console** → F12 → Console tab for errors
3. **Vercel Dashboard** → Project Settings → Environment Variables

