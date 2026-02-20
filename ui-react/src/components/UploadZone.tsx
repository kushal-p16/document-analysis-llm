import { useRef } from "react";

const UploadZone = ({ onFileUpload }: { onFileUpload: (file: File) => void }) => {
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      onFileUpload(file); // ✅ calls backend API
    }
  };

  return (
    <div
      className="glass rounded-3xl p-10 text-center cursor-pointer hover:bg-primary/5 transition"
      onClick={() => fileInputRef.current?.click()}
    >
      <p className="text-lg font-medium text-foreground/70">
        Click to upload a PDF
      </p>
      <p className="text-sm text-muted-foreground mt-2">Max size: 10 MB</p>

      <input
        type="file"
        accept="application/pdf"
        ref={fileInputRef}
        onChange={handleFileSelect}
        className="hidden"
      />
    </div>
  );
};

export default UploadZone;