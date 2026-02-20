import { Loader2 } from "lucide-react";

const LoadingSpinner = ({ text = "Processing PDF…" }: { text?: string }) => (
  <div className="flex flex-col items-center gap-4 py-10 animate-fade-in">
    <Loader2 className="w-10 h-10 text-primary animate-spin" />
    <p className="text-muted-foreground font-medium">{text}</p>
    <div className="w-48 h-1.5 rounded-full overflow-hidden bg-muted">
      <div className="h-full rounded-full shimmer bg-primary/30" style={{ width: "100%" }} />
    </div>
  </div>
);

export default LoadingSpinner;
