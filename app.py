import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))

def predict(data):
    import numpy as np
    prediction = model.predict(data)
    return prediction

st.title('Bitcoin Prediction')

Open = st.number_input('Opening Price', min_value = 0)
High = st.number_input('Highest Price', min_value = 0)
Low = st.number_input('Lowest Price', min_value = 0)
Volume = st.number_input('Volume of Bitcoin in Market', min_value = 0)

features = {'Opening Price' : Open,
            'High' : High,
            'Low' : Low,
            'Volume' : Volume}

features_df = pd.DataFrame([features])
st.table(features_df) 
st.text('It might show prediction not defined. Please ignore it for now.\nI am working on it')
if st.button('Predict the Price'):

    prediction = predict(features_df)

    st.success('The predicted price is {}'.format(prediction))

st.text("This is not an actual predictor! Don't use this while buying bitcoin.")
