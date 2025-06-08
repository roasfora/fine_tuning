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

## 👤 Author

**Your Name**  
📧 your.email@example.com  
🌐 [GitHub](https://github.com/yourusername)  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🛡 License

MIT License – feel free to use, modify, and distribute with attribution.
