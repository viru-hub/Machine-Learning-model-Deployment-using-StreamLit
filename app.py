import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle

pickle_in = open("model.pkl","rb")
classifier= pickle.load(pickle_in)

def Welcome():
    return "Welcome"

def predict_note(variance,skewness,curtosis,entropy):
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Authentication")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("variance","typehere")
    skewness = st.text_input("skewness","typehere")
    curtosis = st.text_input("curtosis","typehere")
    entropy = st.text_input("entropy","typehere")
    result = ""
    if st.button('predict'):
        result = predict_note(variance,skewness,curtosis,entropy)
    st.success('The output is{}'.format(result))

if __name__ =='__main__':
    main()