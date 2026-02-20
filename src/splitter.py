import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt", quiet=True)

def split_into_passages(text, max_words=180):
    sentences = sent_tokenize(text)
    passages = []
    current = ""

    for sentence in sentences:
        if len(current.split()) + len(sentence.split()) < max_words:
            current += " " + sentence
        else:
            passages.append(current.strip())
            current = sentence

    if current:
        passages.append(current.strip())

    return passages
