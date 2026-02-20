# 🚀 Dual Deployment Guide: Vercel + Railway

## Architecture Overview
```
Frontend (React/Vite)  →  Vercel.com
        ↓
        ↓ (API calls)
        ↓
Backend (FastAPI)  →  Railway.app
```

---

## Part 1: Deploy Frontend to Vercel ✅

### Step 1: Go to Vercel
- Visit: https://vercel.com
- Sign in with GitHub

### Step 2: Import Project
- Click **"Add New"** → **"Project"**
- Select **"Import Git Repository"**
- Choose: `kushal-p16/document-analysis-llm`
- Click **"Import"**

### Step 3: Configure Build Settings
- **Framework**: Auto-detected (Vite)
- **Build Command**: `cd ui-react && npm install && npm run build`
- **Output Directory**: `ui-react/dist`
- **Environment Variables**: Add after deploying backend

### Step 4: Deploy
- Click **"Deploy"**
- Wait 2-3 minutes for build to complete
- Your frontend URL: `https://document-analysis-llm.vercel.app`

---

## Part 2: Deploy Backend to Railway 🚂

### Step 1: Create Railway Account
- Visit: https://railway.app
- Sign up with GitHub

### Step 2: Create New Project
- Click **"Create New Project"**
- Select **"Deploy from GitHub repo"**
- Find and select: `kushal-p16/document-analysis-llm`
- Click **"Deploy"**

### Step 3: Configure Service
Railway will automatically:
- Detect Python project
- Read `requirements.txt`
- Use `Dockerfile` to build
- Start the service

### Step 4: Set Environment Variables
In Railway dashboard:
1. Go to **Variables** tab
2. Add: `GROQ_API_KEY=your-actual-groq-api-key`
3. Click **"Save"**
4. Service will auto-redeploy

### Step 5: Get Backend URL
- Go to **Settings** in Railway
- Find **Domain** section
- Copy your Railway URL (e.g., `https://document-analysis-llm-production.up.railway.app`)

---

## Part 3: Connect Frontend to Backend 🔗

### Update Vercel Environment Variable
1. Go to Vercel dashboard
2. Open your project settings
3. Go to **Environment Variables**
4. Add:
   ```
   VITE_API_URL=https://your-railway-url
   ```
   (Replace with your actual Railway backend URL)

5. Click **"Save"** 
6. Vercel will automatically redeploy with the new URL

---

## Testing Your Deployment

### 1. Frontend is Live
- Open: `https://document-analysis-llm.vercel.app`
- You should see the AI PDF Analyst UI

### 2. Backend is Connected
1. Try uploading a PDF
2. If you see:
   - ✅ Summary & keywords → **Backend is working!**
   - ❌ Error message → Check Railway logs

### 3. Debugging API Issues
**If PDF upload fails:**
1. Open browser DevTools (F12)
2. Go to **Network** tab
3. Check if `/upload` request is being sent to correct Railway URL
4. Check Railway logs for errors

---

## 🛠️ What Each Platform Does

### **Vercel (Frontend)**
- Hosts your React app
- Handles all UI interactions
- Makes API calls to Railway backend
- Auto-deploys on GitHub push

### **Railway (Backend)**
- Runs FastAPI server 24/7
- Processes PDF uploads
- Calls Groq API for AI features
- Returns summary + keywords
- Answers questions about PDFs

---

## 📱 How It Works

```
User opens app → Browser loads React from Vercel
                         ↓
User uploads PDF → Frontend sends to Railway backend
                         ↓
Railway processes PDF → Calls Groq AI API
                         ↓
Returns summary + keywords → Frontend displays results
                         ↓
User asks question → Frontend sends to Railway
                         ↓
Railway answers with Groq → Frontend shows answer
```

---

## 🆘 Troubleshooting

### "API endpoint not found"
- ✅ Check Railway backend URL is correct in Vercel env vars
- ✅ Check Railway service is running (green status in dashboard)

### "PDF upload takes too long"
- ✅ Railway free tier might be slow on first request
- ✅ Check Railway logs for errors
- ✅ Upgrade to paid plan if needed

### "GROQ_API_KEY error"
- ✅ Set `GROQ_API_KEY` in Railway environment variables
- ✅ Service will auto-redeploy

### "502 Bad Gateway"
- ✅ Backend service might not be running
- ✅ Check Railway logs
- ✅ Restart service from Railway dashboard

---

## 📊 Costs

- **Vercel**: Free (frontend hosting)
- **Railway**: 
  - Free tier: $5 credit/month (usually enough)
  - Pay-as-you-go after that (~$0.10-1/day for light usage)

---

## 📝 Project Files

```
vercel.json          → Frontend build config (Vercel)
railway.json         → Backend build config (Railway)
Dockerfile           → How to build backend container
requirements.txt     → Python dependencies
fastapi_server.py    → FastAPI app (runs on Railway)
ui-react/            → React frontend (deployed to Vercel)
```

---

## ✅ Deployment Checklist

- [ ] Frontend deployed to Vercel
- [ ] Backend deployed to Railway
- [ ] `GROQ_API_KEY` set in Railway
- [ ] `VITE_API_URL` set in Vercel pointing to Railway
- [ ] Frontend can load at Vercel URL
- [ ] PDF upload works end-to-end
- [ ] AI features working (summary, keywords, Q&A)

---

## 🎉 Success!

Once everything is set up:
- Open your Vercel frontend URL
- Upload a PDF
- Get AI analysis instantly
- Ask questions about the PDF
- Everything works seamlessly!

Your app is now **live and accessible to the world!** 🌍
