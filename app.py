import numpy as np
import streamlit as st
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

sw = stopwords.words('english')
sw.remove('not')
sw = set(sw)
ps = PorterStemmer()


def cleaning_pipeline(review):
    words = word_tokenize(review.lower())
    words = [ps.stem(word) for word in words if word not in sw and word.isalpha()]
    review = " ".join(words)
    return review

def load_model(path):
    with open(path, 'rb') as f:
        cv, model = pickle.load(f)
    
    return cv, model

def predict(text):
    cv, model = load_model("./artifacts/MNBmodel2.pkl")
    cleaned_text = cleaning_pipeline(text)
    text_vect = cv.transform([cleaned_text])
    return model.predict(text_vect)
    

def run():
    st.set_page_config(layout='centered',
                   page_title="Sentiment Predicter")
    st.title("Predicting Movie Review Sentiment")
    st.header('This app is created to predict if the sentiment of a movie review is positive or negative')
    text = st.text_area('Enter text')
    output = ""
    if st.button("Predict"):
        output = predict(text)
        output = str(output[0]) # since its a list, get the 1st item
        if output == '1':
            st.success("The predicted sentiment is positive")
        else:
            st.error("The predicted sentiment is negative")
        st.balloons()        

run()