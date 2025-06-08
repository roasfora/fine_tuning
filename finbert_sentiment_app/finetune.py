import streamlit as st
from predictor import predict_sentiment

st.set_page_config(page_title="📊 Financial Sentiment Analyzer")
st.title("📊 Financial Sentiment Analyzer (Fine-Tuned Only)")

text = st.text_area("Enter a financial headline or news snippet:")

if st.button("Analyze Sentiment"):
    if text.strip():
        try:
            st.write("🔍 Analyzing with fine-tuned model...")
            label, probs = predict_sentiment(text)

            st.subheader("🛠️ Fine-Tuned FinBERT Prediction")
            st.success(f"**Sentiment:** {label.capitalize()}")
            st.write("**Confidence Scores:**")
            st.json({
                "Negative": probs[0],
                "Neutral": probs[1],
                "Positive": probs[2]
            })

        except Exception as e:
            st.error(f"❌ Error during prediction:\n\n{str(e)}")
    else:
        st.warning("⚠️ Please enter some text to analyze.")
