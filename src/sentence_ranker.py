import nltk
from nltk.tokenize import sent_tokenize

def important_sentences(text, top_n=5):
    sentences = sent_tokenize(text)

    # Rank by length + unique word count (simple scoring)
    ranked = sorted(
        sentences,
        key=lambda s: len(set(s.split())) + len(s),
        reverse=True
    )

    return ranked[:top_n]
