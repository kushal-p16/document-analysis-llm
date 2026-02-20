from transformers import pipeline

qa = pipeline("question-answering", model="deepset/bert-large-uncased-whole-word-masking-squad2")

def answer_question(question, context):
    response = qa(
        question=question,
        context=context
    )
    return response["answer"]
