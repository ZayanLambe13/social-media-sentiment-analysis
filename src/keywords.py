from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(texts, top_n=10):
    vectorizer = CountVectorizer(
        stop_words="english",
        max_features=top_n
    )
    X = vectorizer.fit_transform(texts)
    return vectorizer.get_feature_names_out()
