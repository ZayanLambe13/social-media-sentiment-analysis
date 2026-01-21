# Social Media Sentiment Analysis & Real-Time Sentiment Dashboard

This project demonstrates both **offline sentiment analysis** using a historical social media dataset and a **real-time sentiment analysis dashboard** for live user input.

The goal is to clearly separate **data analysis** from **interactive applications**, following industry best practices.

---

## 📂 Project Structure


social-media-sentiment-analysis/
│
├── data/
│ ├── raw/
│ │ └── sentimentdataset.csv
│ └── processed/
│ └── sentiment_results.csv
│
├── notebooks/
│ └── sentiment_analysis.ipynb
│
├── dashboard/
│ └── app.py
│
├── src/
│ ├── preprocessing.py
│ ├── sentiment.py
│ └── keywords.py
│
├── requirements.txt
└── README.md



---

## 🧠 Project Components

### 1️⃣ Offline Sentiment Analysis (Notebook)
- Performed exploratory data analysis (EDA) on a real social media dataset
- Cleaned and preprocessed raw text
- Applied **VADER sentiment analysis**
- Generated sentiment scores and polarity labels
- Compared predicted sentiment with existing dataset labels
- Saved processed results for reference

📓 Notebook used:
notebooks/sentiment_analysis.ipynb


---

### 2️⃣ Real-Time Sentiment Dashboard (Streamlit)
- Accepts **live user text input**
- Instantly computes sentiment score and label
- Maintains session-based history of user inputs
- Dynamically updates sentiment visuals and keyword extraction
- Dashboard visuals are driven **only by user input**
- Dataset is **not used** in real-time visualizations

📊 Dashboard file:
dashboard/app.py



---

## 🛠️ Tech Stack

- Python
- Pandas
- NLP (VADER Sentiment Analysis)
- Scikit-learn (Keyword extraction)
- Streamlit
- Matplotlib

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

