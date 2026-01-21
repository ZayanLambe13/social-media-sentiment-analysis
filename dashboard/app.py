import os
import sys
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- FIX PATH FOR STREAMLIT CLOUD ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from src.preprocessing import clean_text
from src.sentiment import get_sentiment_score, get_sentiment_label
from src.keywords import extract_keywords

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Real-Time Sentiment Analyzer",
    layout="wide"
)

st.title("⚡ Real-Time Sentiment Analyzer (User Input Only)")

# ---------------- SESSION STATE ----------------
if "live_data" not in st.session_state:
    st.session_state.live_data = pd.DataFrame(
        columns=["clean_text", "sentiment_score", "sentiment_label"]
    )

# ---------------- USER INPUT ----------------
st.subheader("✍️ Enter Text")

user_text = st.text_area(
    "Type text below 👇",
    height=120,
    key="user_input"
)

if st.button("Analyze"):
    if user_text.strip():
        clean = clean_text(user_text)
        score = get_sentiment_score(clean)
        label = get_sentiment_label(score)

        new_row = pd.DataFrame([{
            "clean_text": clean,
            "sentiment_score": score,
            "sentiment_label": label
        }])

        st.session_state.live_data = pd.concat(
            [st.session_state.live_data, new_row],
            ignore_index=True
        )

        st.success(f"Sentiment: **{label}** | Score: `{score}`")

# ---------------- REAL-TIME VISUALS ----------------
st.divider()
st.subheader("📊 Live Visuals (Only User Inputs)")

df = st.session_state.live_data

if not df.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Sentiment Distribution")
        fig, ax = plt.subplots()
        df["sentiment_label"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

    with col2:
        st.markdown("### Sentiment Trend")
        fig2, ax2 = plt.subplots()
        ax2.plot(df["sentiment_score"], marker="o")
        ax2.set_xlabel("Input Order")
        ax2.set_ylabel("Sentiment Score")
        st.pyplot(fig2)

    st.divider()
    st.subheader("🔑 Live Keywords")

    keywords = extract_keywords(df["clean_text"], top_n=10)
    st.write(", ".join(keywords))

else:
    st.info("Enter text and click Analyze to generate live visuals.")
