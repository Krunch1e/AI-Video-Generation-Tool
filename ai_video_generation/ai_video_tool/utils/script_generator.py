from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_script(title, description):
    # Create prompt for GPT-2 (without including the "Generate a script..." part in the output)
    prompt = f"Generate a script based on the title: {title} and description: {description}"

    # Encode the prompt and generate text
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode and return the script, removing the first part of the prompt from the result
    script = tokenizer.decode(outputs[0], skip_special_tokens=True)
    script = script[len(prompt):]  # Remove the prompt part from the script
    return script.strip()  # Clean up any extra spaces
