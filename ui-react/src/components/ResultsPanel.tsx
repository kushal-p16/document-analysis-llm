import { useState } from "react";
import { FileText, Tag, MessageCircle, Send, Bot, Sparkles } from "lucide-react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

const API = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const ResultsPanel = ({ fileName, pdfData }: { fileName: string; pdfData: any }) => {
  const [question, setQuestion] = useState("");
  const [thinking, setThinking] = useState(false);
  const [answer, setAnswer] = useState("");

  // Send Q&A request to backend
  const handleAsk = async () => {
    if (!question.trim()) return;

    setThinking(true);
    setAnswer("");

    try {
      const res = await fetch(`${API}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question,
          passages: pdfData?.passages || [],
        }),
      });

      const data = await res.json();

      if (data?.status && data.status !== "success") {
        const msg = data.message || "Unknown backend error";
        setAnswer(`⚠️ ${msg}`);
      } else if (data?.answer) {
        setAnswer(data.answer);
      } else {
        setAnswer("⚠️ Unexpected response from backend");
      }
    } catch (err: any) {
      console.error(err);
      setAnswer(`⚠️ ${err?.message || String(err)}`);
    }

    setThinking(false);
  };

  return (
    <div className="space-y-6 animate-fade-up">

      {/* File info */}
      <div className="glass rounded-2xl px-5 py-3 flex items-center gap-3">
        <FileText className="w-5 h-5 text-primary shrink-0" />
        <span className="text-sm font-medium truncate">{fileName}</span>
        <span className="ml-auto pill text-xs !py-1 !px-3">Analyzed</span>
      </div>

      {/* Summary */}
      <section className="glass rounded-3xl p-6 space-y-3">
        <div className="flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-primary" />
          <h2 className="text-lg font-display font-semibold">Summary</h2>
        </div>
        <div className="text-muted-foreground leading-relaxed text-sm">
          <ReactMarkdown remarkPlugins={[remarkGfm]}>{pdfData?.summary || ""}</ReactMarkdown>
        </div>
      </section>

      {/* Keywords */}
      <section className="glass rounded-3xl p-6 space-y-3">
        <div className="flex items-center gap-2">
          <Tag className="w-5 h-5 text-accent" />
          <h2 className="text-lg font-display font-semibold">Keywords</h2>
        </div>
        <div className="flex flex-wrap gap-2">
          {Array.isArray(pdfData?.keywords) && pdfData.keywords.map((kw: string) => (
            <span key={kw} className="pill">
              {kw}
            </span>
          ))}
        </div>
      </section>

      {/* Q&A */}
      <section className="glass rounded-3xl p-6 space-y-4">
        <div className="flex items-center gap-2">
          <MessageCircle className="w-5 h-5 text-secondary" />
          <h2 className="text-lg font-display font-semibold">Ask a Question</h2>
        </div>

        <div className="flex gap-2">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleAsk()}
            placeholder="Ask anything about this PDF…"
            className="flex-1 bg-muted/50 border border-border rounded-xl px-4 py-3 text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary/40 transition-all"
          />
          <button
            onClick={handleAsk}
            className="shrink-0 w-12 h-12 rounded-xl bg-primary text-primary-foreground flex items-center justify-center hover:opacity-90 transition-opacity"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>

        {/* Thinking animation */}
        {thinking && (
          <div className="flex items-center gap-3 animate-fade-in">
            <div className="w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center">
              <Bot className="w-4 h-4 text-primary animate-pulse" />
            </div>
            <span className="text-sm text-muted-foreground">Thinking…</span>
          </div>
        )}

        {/* Final answer */}
        {!thinking && answer && (
          <div className="flex gap-3 animate-fade-up">
            <div className="w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center shrink-0 mt-1">
              <Bot className="w-4 h-4 text-primary" />
            </div>
            <div className="bot-bubble">
              <div className="text-sm leading-relaxed">
                <ReactMarkdown remarkPlugins={[remarkGfm]}>{answer || ""}</ReactMarkdown>
              </div>
            </div>
          </div>
        )}
      </section>
    </div>
  );
};

export default ResultsPanel;