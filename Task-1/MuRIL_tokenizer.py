from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

# Specify the MuRIL model and tokenizer
model_name = "google/muril-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Example text
text = "MuRIL is a multilingual [MASK] model."

# Tokenize and get predictions
tokens = tokenizer(text, return_tensors="pt")
outputs = model(**tokens)
predictions = outputs.logits.argmax(-1)

# Decode predictions
decoded_predictions = tokenizer.batch_decode(predictions)[0]

print(f"Input Text: {text}")
print(f"Predictions: {decoded_predictions}")
