from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_questions(passage, num_q=3):
    prompt = f"Generate {num_q} questions from this text:\n{passage}"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=200
    )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Split results into questions
    questions = [q.strip() for q in text.split("?") if q.strip()]
    questions = [q + "?" for q in questions]

    return questions[:num_q]
