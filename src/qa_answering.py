from transformers import pipeline

qa = pipeline(
    "question-answering",
    model="deepset/bert-large-uncased-whole-word-masking-squad2"
)

def answer_question(question, passage):
    answer = qa({
        "question": question,
        "context": passage
    })
    return answer["answer"]
