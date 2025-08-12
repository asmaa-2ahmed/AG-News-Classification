import os
from joblib import load
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
stop_words = set(stopwords.words("english"))

# Model Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPELINE_PATH = os.path.join(BASE_DIR, "src", "assets", "logistic_regression_pipe.joblib")

# Load the saved model
if not os.path.exists(PIPELINE_PATH):
    raise FileNotFoundError(f"❌ Model file not found at: {PIPELINE_PATH}")

try:
    pipeline = load(PIPELINE_PATH)
    print(f"✅ Model loaded successfully from {PIPELINE_PATH}")
except Exception as e:
    raise RuntimeError(f"❌ Failed to load model: {e}")
