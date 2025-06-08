# 📊 FinBERT Financial Sentiment Analyzer

A financial sentiment classification app that fine-tunes FinBERT to detect **positive**, **neutral**, or **negative** sentiment in financial headlines or statements. Built using Hugging Face Transformers and Streamlit, the app is fully local and customizable.

---

## 🚀 Features

- ✅ Fine-tune [FinBERT (ProsusAI)](https://huggingface.co/ProsusAI/finbert) on your own financial dataset
- ✅ Analyze sentiment using the fine-tuned model
- ✅ User-friendly Streamlit interface
- ✅ Returns sentiment and class confidence scores
- ✅ Runs 100% locally after setup

---

## 🧱 Project Structure

```
finbert_sentiment_app/
├── app.py                      # Streamlit app UI
├── predictor.py                # Sentiment prediction logic
├── finetune.py                 # Fine-tuning script for FinBERT
│
├── models/
│   └── finbert-finetuned/      # Fine-tuned model (generated)
│
├── data/
│   └── financial_texts.csv     # Input data for training
│
├── requirements.txt            # Dependencies list
├── .gitignore                  # Files/folders to ignore in Git
└── README.md                   # Project overview
```

---

## 💾 Dataset Format

Ensure your `data/financial_texts.csv` file looks like:

| text                                      | label     |
|------------------------------------------|-----------|
| Apple stock soars after earnings report. | positive  |
| Market remains unchanged amid uncertainty| neutral   |
| Oil prices fall sharply in early trading | negative  |

Valid labels: `positive`, `neutral`, `negative`

---

## 📦 Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/finbert-sentiment-analyzer.git
   cd finbert_sentiment_app
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate         # On Windows
   # or
   source venv/bin/activate        # On macOS/Linux

   pip install -r requirements.txt
   ```

---

## 🧠 Fine-Tune FinBERT

Train the model using your dataset:

```bash
python finetune.py
```

The fine-tuned model will be saved under `models/finbert-finetuned/`.

---

## 🚀 Run the Streamlit App

Start the web app locally:

```bash
streamlit run app.py
```

Then open your browser at:  
[http://localhost:8501](http://localhost:8501)

---

## ✅ Example

**Input:**
```
Tech stocks rally as the Fed signals a pause in interest rate hikes.
```

**Output:**
```
Sentiment: Positive
Confidence:
{
  "Negative": 0.02,
  "Neutral": 0.13,
  "Positive": 0.85
}
```

---

## 📚 Requirements

```
transformers
datasets
torch
scikit-learn
pandas
streamlit
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🛠 Future Improvements

- [ ] Add base vs fine-tuned model comparison
- [ ] Batch file input support
- [ ] Sentiment trend graphs
- [ ] Save analysis logs to CSV

---


## 🛡 License

MIT License – feel free to use, modify, and distribute with attribution.


---

## 📰 News Scraping and Sentiment Labeling Pipeline

This project includes a module to scrape financial news from the [Finnhub API](https://finnhub.io/) and label each headline using **FinBERT** (a RoBERTa-based financial sentiment model).

### 🧩 Part 1 — Scrape News Headlines

**Script**: `scraping_finance/fetch_finnhub_news.py`

This script:

- Uses your **Finnhub API key**
- Fetches recent news headlines for selected **S&P 500 tickers**
- Saves the headlines and metadata to a CSV

**Run:**
```bash
python scraping_finance/fetch_finnhub_news.py
```

**Output Example:**
```
scraping_finance/data/finnhub_news_YYYYMMDD.csv
```

### 🧠 Part 2 — Sentiment Labeling with FinBERT

**Script**: `scraping_finance/label_with_finbert.py`

This script:

- Loads the scraped CSV
- Applies the RoBERTa-based FinBERT model
- Labels each headline with a sentiment: `positive`, `neutral`, or `negative`
- Saves the cleaned and labeled dataset

**Run:**
```bash
python scraping_finance/label_with_finbert.py
```

**Output:**
```
finbert_sentiment_app/data/financial_texts.csv
```

This CSV file is then used in `finetune.py` for training your custom model.

---

## 🔁 Workflow Summary

```bash
# 1. Scrape financial headlines
python scraping_finance/fetch_finnhub_news.py

# 2. Label headlines with FinBERT
python scraping_finance/label_with_finbert.py

# 3. Fine-tune sentiment model
python finbert_sentiment_app/finetune.py

# 4. Launch UI
streamlit run finbert_sentiment_app/app.py
```
