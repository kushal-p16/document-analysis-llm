from transformers import pipeline

ner_model = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

def extract_entities(text):
    return ner_model(text)
