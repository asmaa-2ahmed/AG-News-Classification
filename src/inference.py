import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
from src.config import pipeline, stop_words

# Label map
label_map = {0: "World", 1: "Sports", 2: "Business", 3: "Sci/Tech"}

# -------- Preprocessing --------
def preprocess_text(text: str) -> str:
    """
    Clean and preprocess input text for prediction.
    """
    text = re.sub(r'<.*?>', '', text)  # remove HTML tags
    text = re.sub(r'[^a-zA-Z]', ' ', text)  # keep only letters
    text = text.lower()

    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    tokens = [
        lemmatizer.lemmatize(w)
        for w in tokens
        if w not in stop_words and w not in string.punctuation
    ]
    return ' '.join(tokens)

def predict(title: str, description: str) -> int:
    if not title or not description:
        raise ValueError("❌ Both title and description must be provided.")
    
    combined_text = f"{title} {description}"
    clean_text = preprocess_text(combined_text)
    return pipeline.predict([clean_text])[0]

def predict_label(title: str, description: str) -> str:
    label_index = predict(title, description)
    return label_map[label_index]