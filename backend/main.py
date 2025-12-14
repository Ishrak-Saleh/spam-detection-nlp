
#py -m pip install nltk
#py -m pip install streamlit
import streamlit as st
import pickle
import string
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from pathlib import Path



ps = PorterStemmer()

def transform_text(text):
    #Lowering case
    text = text.lower()
    
    #Tokenization
    text = nltk.word_tokenize(text)
    
    #Removing special characters
    c = []
    for char in text:
        if char.isalnum(): c.append(char)
    
    #Removing stop words and punctuation
    text = c[:]
    c.clear()
    for char in text:
        if char not in stopwords.words('english') and char not in punctuation:
            c.append(char)
    
    #Stemming
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()
    text = c[:]
    c.clear()
    for char in text:
        c.append(ps.stem(char))
    return " ".join(c)


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"

tfidf = pickle.load(open(MODEL_DIR / "vectorizer.pkl", "rb"))
model = pickle.load(open(MODEL_DIR / "model.pkl", "rb"))

st.title('SMS Spam Detector')

input_sms = st.text_area('Enter message')

if st.button('Predict'):

    #preprocess
    transform_sms = transform_text(input_sms)

    #vectorize
    vector_input = tfidf.transform([transform_sms])

    #predict
    result = model.predict(vector_input)[0]

    #display
    if result == 1: st.header("Spam")
    else: st.header("Not Spam")