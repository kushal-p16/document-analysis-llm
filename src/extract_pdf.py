import pdfplumber

def extract_text(pdf_path, output_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print("✔ PDF text extracted.")
