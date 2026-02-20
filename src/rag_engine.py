from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def build_vector_store(passages):
    # Encode passages
    vectors = model.encode(passages, convert_to_numpy=True)

    # SAFETY CHECK — prevent crash
    if vectors is None or len(vectors) == 0:
        raise ValueError("❌ No embeddings generated. PDF text may be empty or unreadable.")

    # Ensure 2D shape
    vectors = np.array(vectors)
    if len(vectors.shape) != 2:
        raise ValueError("❌ Invalid embeddings shape. Something went wrong while encoding.")

    dim = vectors.shape[1]  # embedding size (384)

    # Build FAISS index
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    return index, vectors


def rag_answer(query, passages, index):
    # Encode query
    q_vec = model.encode([query], convert_to_numpy=True)

    # Safety check
    if q_vec is None or len(q_vec) == 0:
        return {"answer": "Query could not be processed.", "passage": ""}

    # Search top-1 result
    D, I = index.search(q_vec, k=1)

    best_passage = passages[I[0][0]]

    # Use QA model
    from answerer import answer_question
    final_answer = answer_question(query, best_passage)

    return {"answer": final_answer, "passage": best_passage}