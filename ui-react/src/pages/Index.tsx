import { useState } from "react";
import { Brain } from "lucide-react";
import UploadZone from "@/components/UploadZone";
import LoadingSpinner from "@/components/LoadingSpinner";
import ResultsPanel from "@/components/ResultsPanel";

// Backend API - uses same origin on Vercel or localhost for local dev
const API = import.meta.env.VITE_API_URL || "";

const Index = () => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [analyzed, setAnalyzed] = useState(false);
  const [pdfData, setPdfData] = useState<any>(null);

  // 🔥 Fixed version — correctly checks backend status
  const handleUpload = async (f: File) => {
    setFile(f);
    setLoading(true);
    setAnalyzed(false);

    const formData = new FormData();
    formData.append("file", f);

    try {
      const res = await fetch(`${API}/upload`, {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      console.log("Backend response:", data);

      if (data.status !== "success") {
        const msg = data.message || "Upload failed on backend!";
        alert(msg);
        setLoading(false);
        return;
      }

      setPdfData(data); // contains summary + keywords
      setAnalyzed(true);
    } catch (err) {
      console.error("Upload error:", err);
      alert("Upload failed. Check backend!");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen gradient-bg relative overflow-hidden">
      {/* Ambient blobs */}
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute -top-40 -left-40 w-[500px] h-[500px] rounded-full bg-primary/10 blur-[120px]" />
        <div className="absolute top-1/2 -right-40 w-[400px] h-[400px] rounded-full bg-accent/10 blur-[120px]" />
        <div className="absolute bottom-0 left-1/3 w-[350px] h-[350px] rounded-full bg-secondary/10 blur-[120px]" />
      </div>

      <div className="relative z-10 max-w-2xl mx-auto px-4 py-16 md:py-24">
        {/* Header */}
        <header className="text-center mb-12 space-y-4">
          <div className="inline-flex items-center gap-2 pill mb-2">
            <Brain className="w-4 h-4" />
            <span>Powered by AI</span>
          </div>
          <h1 className="text-4xl md:text-5xl font-display font-bold glow-text leading-tight">
            AI PDF Analyst
          </h1>
          <p className="text-lg font-display font-medium text-foreground/80">
            document-analysis-llm – kushal p
          </p>
          <p className="text-muted-foreground max-w-md mx-auto">
            Upload any PDF and get instant summaries, keywords, and AI answers.
          </p>
        </header>

        {/* Main content */}
        {!file && !loading && <UploadZone onFileUpload={handleUpload} />}
        {loading && <LoadingSpinner />}
        {analyzed && file && (
          <div className="space-y-6">
            <ResultsPanel fileName={file.name} pdfData={pdfData} />

            <button
              onClick={() => {
                setFile(null);
                setAnalyzed(false);
              }}
              className="mx-auto block text-sm text-muted-foreground hover:text-foreground transition-colors underline underline-offset-4"
            >
              Upload another PDF
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Index;