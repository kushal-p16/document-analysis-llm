from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(text):
    text = text[:2000]
    prompt = "Summarize the following text:\n" + text

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=200,
        min_new_tokens=40
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
