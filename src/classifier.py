from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

def classify_text(text):
    labels = [
        "Legal", "Business", "Technology", "Privacy",
        "Finance", "Service Agreement", "Terms & Conditions"
    ]

    result = classifier(text, candidate_labels=labels)
    return result
