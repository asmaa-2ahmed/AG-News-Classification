# 📰 AG News Classification Project

![Banner Image](src/assets/image.png)

## 🌟 Overview
A machine learning-powered web application that automatically classifies news articles into four categories:  
🌍 **World** | 🏅 **Sports** | 💼 **Business** | 🔬 **Sci/Tech**

Built with **Python**, **Scikit-learn**, **XGBoost**, and **TensorFlow**, this project demonstrates:
- Natural Language Processing (NLP) techniques
- Comparison between classical ML and deep learning models
- Production-ready deployment workflow
- Clean and responsive UI design

---

## 🚀 Key Features

### 🔍 Core Functionality
- **Text Classification**: Predicts news categories from headlines and descriptions
- **High Accuracy**: Achieved over **91%** accuracy on test data
- **Fast Inference**: Logistic Regression processes inputs in under **0.5 seconds**

### 🎨 User Experience
- Dark mode interface for eye comfort
- Responsive layout (desktop & mobile)
- Minimal, clean input/output workflow

### ⚙️ Technical Highlights
- Custom text preprocessing pipeline
- TF-IDF vectorization for classical ML
- RNN, GRU, and LSTM architectures for deep learning comparison
- Model persistence with Joblib

---

## 📂 Project Structure
```
project/
│
├── src/
│   ├── assets/
│   │   └── logistic_regression.joblib
│   ├── notebook/
│   │    └── AG_News_clf.ipynb
│   ├── config.py
│   ├── inference.py
│   ├── schemas.py
│   ├── views/
│   │    └── app.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Steps
```bash
# Clone the repository
git clone https://github.com/asmaa-2ahmed/AG-News-Classification.git
cd AG-News-Classification

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download(['stopwords', 'punkt', 'wordnet'])"
```

---

## 🏃‍♂️ Running the Application
```bash
streamlit run main.py
```
The app will open in your browser at **http://localhost:8501**.

---

## 🧠 Model Details

### 📊 Training Data
- **Dataset**: AG News Classification Dataset (120,000 training / 7,600 test samples)
- **Categories**: World, Sports, Business, Sci/Tech
- **Balanced classes**

### 🏆 Performance Metrics
| Model               | Accuracy  | F1-score  | Train Time  | Inference Time |
|---------------------|-----------|-----------|-------------|----------------|
| Logistic Regression | **91.56%**| **0.9154**| 13.8s       | **0.48s**      |
| XGBoost             | 91.03%    | 0.9100    | 542.2s      | 1.02s          |
| RNN                 | 91.49%    | 0.9148    | 1560.8s     | 13.66s         |
| GRU                 | 91.79%    | 0.9178    | 4485.8s     | 41.07s         |
| LSTM                | 91.68%    | 0.9167    | 3375.2s     | 81.98s         |

**Final Choice:** Logistic Regression — best trade-off between performance, speed, and deployment cost.

---

## 🧹 Preprocessing Pipeline
- Remove HTML tags
- Clean special characters
- Lowercasing
- Tokenization
- Lemmatization
- Stopword removal

---

## 📎 Appendix: Sample Classifications
| Category   |  Title                                                       |  Description |
|------------|---------------------------------------------------------------------|---------------------|
| 🌍 **World** | Global Summit Addresses Climate Change Crisis | World leaders from 150 nations gathered in Paris today to sign a historic agreement committing to carbon neutrality by 2050. The treaty includes unprecedented funding for developing countries to transition to renewable energy. |
| ⚽ **Sports** | Argentina Wins FIFA World Cup in Penalty Shootout Thriller | In a dramatic finale, Lionel Messi led Argentina to victory against France 4-2 on penalties after a 3-3 draw in extra time. The match is being hailed as one of the greatest World Cup finals in history. |
| 💼 **Business** | Tech Giant Apple Unveils Revolutionary AI Chip | Apple's new M4 processor, featuring breakthrough neural engine capabilities, promises 50% faster machine learning performance. Analysts predict this will redefine mobile computing and boost Apple's stock value. |
| 🔬 **Sci/Tech** | NASA Discovers Earth-Like Planet in Habitable Zone | Astronomers using the James Webb Space Telescope identified Kepler-452b, a planet with liquid water and atmospheric conditions that could support life. This marks the most promising exoplanet discovery to date. |

---

## 🤝 Contributing

We welcome contributions!
---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
