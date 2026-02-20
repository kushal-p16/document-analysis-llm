from extract_pdf import extract_text
from summarizer import summarize_text
from splitter import split_into_passages
from question_generator import generate_questions
from answerer import answer_question
from rag_engine import build_vector_store, rag_answer
from keyword_extractor import extract_keywords  # NEW STEP 5

# -----------------------------
# PATHS
# -----------------------------
pdf_path = "../data/google_terms.pdf"
text_path = "../data/extracted.txt"

# -----------------------------
# 1. Extract PDF Text
# -----------------------------
print("\n===== STEP 1: Extracting PDF =====")
extract_text(pdf_path, text_path)

# Read extracted text
with open(text_path, "r", encoding="utf-8") as f:
    text = f.read()

# -----------------------------
# 2. Summarize Text
# -----------------------------
print("\n===== STEP 2: SUMMARY =====")
summary = summarize_text(text)
print(summary)

# -----------------------------
# 3. Split into Passages
# -----------------------------
print("\n===== STEP 3: Splitting into Passages =====")
passages = split_into_passages(text)
print(f"\nTotal passages: {len(passages)}")

# -----------------------------
# 4. Build Vector Store (RAG)
# -----------------------------
print("\n===== STEP 4: Building Vector Store (RAG) =====")
index, vectors = build_vector_store(passages)
print("Vector store ready ✔")

# -----------------------------
# 5. Keyword Extraction
# -----------------------------
print("\n===== STEP 5: Extracting Keywords =====")
for i, p in enumerate(passages[:5]):  # only first 5 passages
    keys = extract_keywords(p)
    print(f"\nPassage {i+1} Keywords:", keys)

# -----------------------------
# 6. Question Generation (Optional)
# -----------------------------
print("\n===== STEP 6: Sample Questions from Passage 1 =====")
sample_qs = generate_questions(passages[0])
for q in sample_qs:
    print("-", q)

# -----------------------------
# 7. User RAG Question Answering
# -----------------------------
print("\n===== STEP 7: Ask ANY Question About the PDF =====")

while True:
    user_q = input("Enter your question: ").strip()
    
    if user_q == "":
        print("⚠️ Please type a question. Don't leave it empty!")
        continue
    break

result = rag_answer(user_q, passages, index)

print("\n===== RAG ANSWER =====")
print("Answer:", result["answer"])

print("\n--- Relevant Passage ---")
print(result["passage"])