from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_script(title, description):
    prompt = f"Title: {title}\nDescription: {description}\nScript:"
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)
    script = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return script[len(prompt):].strip()