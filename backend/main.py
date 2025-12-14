import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from string import punctuation
from pathlib import Path

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"

tfidf = pickle.load(open(MODEL_DIR / "vectorizer.pkl", "rb"))
model = pickle.load(open(MODEL_DIR / "model.pkl", "rb"))  #Logistic Regression


def transform_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)

    clean_tokens = []
    for word in tokens:
        if word.isalnum() and word not in stopwords.words('english'): 
            clean_tokens.append(ps.stem(word))

    return " ".join(clean_tokens)


def predict_spam(text):
    transformed = transform_text(text)
    vector_input = tfidf.transform([transformed])
 
    #Get the probability scores: model.predict_proba returns [[prob_ham, prob_spam]]
    probabilities = model.predict_proba(vector_input)[0]
    
    #prob_spam is the score for class 1 (Spam)
    prob_spam = probabilities[1] 
    
    #Get the final classification (0 or 1)
    prediction = model.predict(vector_input)[0]
    

    return prediction, prob_spam
    