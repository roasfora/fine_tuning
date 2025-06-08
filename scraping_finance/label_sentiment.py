import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

# Load RoBERTa-based FinBERT
model_name = "ProsusAI/finbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

# Sentiment labels
labels = ["negative", "neutral", "positive"]

# Load scraped headlines
input_path = "scraping_finance/data/finnhub_news_20250608.csv"
df = pd.read_csv(input_path)

# Handle missing or blank headlines safely
df = df[df["headline"].notna() & df["headline"].str.strip().astype(bool)]

# Sentiment prediction function
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
        pred = torch.argmax(logits, dim=1).item()
        return labels[pred]

# Apply sentiment analysis
print("Running sentiment analysis with RoBERTa-based FinBERT...")
df["label"] = df["headline"].apply(lambda x: predict_sentiment(str(x)))

# Save only the necessary columns
final_df = df[["headline", "label"]].rename(columns={"headline": "text"})

# Ensure output directory exists
output_dir = "finbert_sentiment_app/data"
os.makedirs(output_dir, exist_ok=True)

# Save to CSV
output_file = os.path.join(output_dir, "financial_texts.csv")
final_df.to_csv(output_file, index=False)

print(f"Sentiment-labeled dataset saved to:\n{output_file}")
