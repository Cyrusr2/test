# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import streamlit as st
import pandas as pd
from io import StringIO
from PIL import Image
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('prediction') 

image = Image.open('header.jpg')

st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto") 

st.title("Lung Cancer Survival Prediction System")

st.caption("The following is a prototype survival prediction model that accepts genomic data and outputs a survivability in the form of a number between 0 and 1. A number greater than 0.5 indicates a survivability greater than 50%, while a number below 0.5 indicates a survivability less than 50%. Please upload your data in a .txt file format.", unsafe_allow_html=False) 

uploaded_file=st.file_uploader("Upload DNA Sequence Here", type=['txt'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)


if uploaded_file is not None:
   dataframe = pd.read_csv(uploaded_file)
   st.write(dataframe)
    
   uploadbutton=st.button('Upload',disabled= False)
     
       
if st.button('Predict!'):
    df = pd.DataFrame(dataframe.dict(), index=[30])
    df['RPPA_Y2K'], df['RPPA_YZY'] = [1.065743, 0.693467]
    y = model.predict(df)
    y = [0 if val < 0.5 else 1 for val in y]
    if y == 1:
        survival = 'You will survive.'
    if y == 0:
        survival = 'You will wont survive.'
    st.write(survival) ##begin prediction and output results here
        
st.header('FAQ', anchor=None)

st.caption('WIP')

st.header('Acknowledgements', anchor=None)

st.caption('WIP')  

