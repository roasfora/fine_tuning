from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Use only your fine-tuned model
model_path = "models/finbert-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()

labels = ["negative", "neutral", "positive"]

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.nn.functional.softmax(logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
        return labels[pred], [round(p, 4) for p in probs[0].tolist()]
