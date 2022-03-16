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
from pydantic import BaseModel
import json
from tensorflow.keras.models import load_model

model = load_model('prediction') 

image = Image.open('header.jpg')

st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto") 

st.title("Lung Cancer Survival Prediction System")

st.caption("The following is a prototype survival prediction model that accepts genomic data and outputs a survivability in the form of a number between 0 and 1. A number greater than 0.5 indicates a survivability greater than 50%, while a number below 0.5 indicates a survivability less than 50%. Please upload your data in a .txt file format.", unsafe_allow_html=False) 

uploaded_file=st.file_uploader("Upload DNA Sequence Here", type=['txt'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

class Userdata(BaseModel):
    RPPA_HSPA1A : float
    RPPA_XIAP : float
    RPPA_CASP7 : float
    RPPA_ERBB3 :float
    RPPA_SMAD1 : float
    RPPA_SYK : float
    RPPA_STAT5A : float
    RPPA_CD20 : float
    RPPA_AKT1_Akt :float
    RPPA_BAD : float
    RPPA_PARP1 : float
    RPPA_MSH2 : float
    RPPA_MSH6 : float
    RPPA_ACACA : float
    RPPA_COL6A1 : float
    RPPA_PTCH1 : float
    RPPA_AKT1 : float
    RPPA_CDKN1B : float
    RPPA_GATA3 : float
    RPPA_MAPT : float
    RPPA_TGM2 : float
    RPPA_CCNE1 : float
    RPPA_INPP4B : float
    RPPA_ACACA_ACC1 : float
    RPPA_RPS6 : float
    RPPA_VASP : float
    RPPA_CDH1 : float
    RPPA_EIF4EBP1 : float
    RPPA_CTNNB1 : float
    RPPA_XBP1 : float
    RPPA_EIF4EBP1_4E : float
    RPPA_PCNA : float
    RPPA_SRC : float
    RPPA_TP53BP1 : float
    RPPA_MAP2K1 : float
    RPPA_RAF1 : float
    RPPA_MET : float
    RPPA_TP53 : float
    RPPA_YAP1 : float
    RPPA_MAPK8 : float
    RPPA_CDKN1B_p27 : float
    RPPA_FRAP1 : float
    RPPA_RAD50 : float
    RPPA_CCNE2 : float
    RPPA_SNAI2 : float
    RPPA_PRKCA_PKC : float
    RPPA_PGR : float
    RPPA_ASNS : float
    RPPA_BID : float
    RPPA_CHEK2 : float
    RPPA_BCL2L1 : float
    RPPA_RPS6 : float
    RPPA_EGFR : float
    RPPA_PIK3CA : float
    RPPA_BCL2L11 : float
    RPPA_GSK3A : float
    RPPA_DVL3 : float
    RPPA_CCND1 : float
    RPPA_RAB11A : float
    RPPA_SRC_Src_pY416 :float
    RPPA_BCL2L111 : float
    RPPA_ATM : float
    RPPA_NOTCH1 : float
    RPPA_C12ORF5 : float
    RPPA_MAPK9 : float
    RPPA_FN1 : float
    RPPA_GSK3A_GSK3B : float
    RPPA_CDKN1B_p27_pT198 : float
    RPPA_MAP2K1_MEK1 : float
    RPPA_CASP8 : float
    RPPA_PAI : float
    RPPA_CHEK1 : float
    RPPA_STK11 : float
    RPPA_AKT1S1 : float
    RPPA_WWTR1 : float
    RPPA_CDKN1A : float
    RPPA_KDR : float
    RPPA_CHEK2_2 : float
    RPPA_EGFR_pY1173 : float
    RPPA_EGFR_pY992 : float
    RPPA_IGF1R : float
    RPPA_YWHAE : float
    RPPA_RPS6KA1 : float
    RPPA_TSC2 : float
    RPPA_CDC2 : float
    RPPA_EEF2 : float
    RPPA_NCOA3 : float
    RPPA_FRAP1 : float
    RPPA_AR : float
    RPPA_GAB2 : float
    RPPA_YBX1 : float
    RPPA_ESR1 : float
    RPPA_RAD51 : float
    RPPA_SMAD4 : float
    RPPA_CDH3 : float
    RPPA_CDH2 : float
    RPPA_FOXO3 : float
    RPPA_ERBB2_HER : float
    RPPA_BECN1 : float
    RPPA_CASP9 : float
    RPPA_SETD2 : float
    RPPA_SRC_Src_mv : float
    RPPA_GSK3A_alpha : float
    RPPA_YAP1_pS127 : float
    RPPA_PRKCA_alpha : float
    RPPA_PRKAA1 : float
    RPPA_RAF1_pS338 : float
    RPPA_MYC : float
    RPPA_PRKAA1_AMPK : float
    RPPA_ERRFI1_MIG : float
    RPPA_EIF4EBP1_2 : float
    RPPA_STAT3 : float
    RPPA_AKT1_AKT2_AKT3 : float
    RPPA_NF2 : float
    RPPA_PECAM1 : float
    RPPA_BAK1 : float
    RPPA_IRS1 : float
    RPPA_PTK2 : float
    RPPA_ERBB3_2 : float
    RPPA_FOXO3_a : float
    RPPA_RB1_Rb : float
    RPPA_MAPK14_p38 : float
    RPPA_NFKB1 : float
    RPPA_CHEK1_Chk1 : float
    RPPA_LCK : float
    RPPA_XRCC5 : float
    RPPA_PARK7 : float
    RPPA_DIABLO : float
    RPPA_CTNNA1 : float
    RPPA_ESR1_ER : float
    RPPA_IGFBP2 : float
    RPPA_STMN1 : float
    RPPA_WWTR1_TAZ : float
    RPPA_CASP3 : float
    RPPA_JUN : float
    RPPA_CCNB1 : float
    RPPA_CLDN7 : float
    RPPA_PXN : float
    RPPA_RPS6KB1_p : float
    RPPA_KIT : float
    RPPA_CAV1 : float
    RPPA_PTEN : float
    RPPA_BAX : float
    RPPA_SMAD3 : float
    RPPA_ERBB2 : float
    RPPA_MET_c : float
    RPPA_ERCC1 : float
    RPPA_MAPK14 : float
    RPPA_BIRC2 : float
    RPPA_PIK3R1 : float
    RPPA_BCL2 : float
    RPPA_PEA : float
    RPPA_EEF2K : float
    RPPA_RPS6KB1_p70 : float
    RPPA_MRE11A : float
    RPPA_KRAS : float
    RPPA_ARID1A : float
    RPPA_YBX1_yb : float
    RPPA_NOTCH3 : float
    RPPA_EIF4EBP1_3 : float
    RPPA_XRCC1 : float
    RPPA_ANXA1 : float
    RPPA_CD49 : float
    RPPA_SHC1 : float
    RPPA_PDK1 : float
    RPPA_EIF4E : float
    RPPA_MAPK1_MAPK3 : float
    RPPA_PTGS2 : float
    RPPA_PRKCA : float
    RPPA_EGFR_egfr : float
    RPPA_RAB25 : float
    RPPA_RB1 : float
    RPPA_MAPK1 : float
    RPPA_TFF1 : float
        
    class config:
        orm_mode = True
if uploaded_file is not None:
   dataframe = pd.read_csv(uploaded_file)
   
   st.write(dataframe)
    
   uploadbutton=st.button('Upload',disabled= False)

  
       
if st.button('Predict!'):
    df = pd.DataFrame(Userdata.dict(), index=[30])
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

