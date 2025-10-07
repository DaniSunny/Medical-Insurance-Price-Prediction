import streamlit as st
import numpy as np
import pandas as pd
import joblib
import sklearn

data=joblib.load('D:\Project\Medical_Insurance\medical_insurance.pkl')


st.title("Medical Insurance Price Predictor")
st.image("https://images.apollo247.in/pd-cms/cms/2023-02/health-insurance_0.jpg")
st.markdown("""
            It is a Machine Learning Model that predict the amount of Insurance can 
            be give to a particular person based on some features(Age,Sex,BMI,Children,Smoker,Region)
             
            

<b> Age </b>: age of primary beneficiary

<b> Sex </b>: insurance contractor gender, female, male

<b> BMI </b>: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,
objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9

<b> Children </b>: Number of children covered by health insurance / Number of dependents

<b> Smoker </b> : Smoking or not

<b> Region </b>: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.

<b> Charges </b>: Individual medical costs billed by health insurance""",unsafe_allow_html=True)

with st.sidebar:
    age=st.number_input("Age",18,75)

    sex=st.selectbox("Sex",['Male','Female'])
    sex=data['encode']['sex'].transform([sex.lower()])[0]

    bmi=st.number_input('BMI',14.0000,75.0000,format="%.4f")

    children=st.number_input("No.of childrens",0,10)

    smoker=st.selectbox("Smoker(Yes/No)",['Yes','No'])
    smoker=data['encode']['smoker'].transform([smoker.lower()])[0]

    user_region=st.selectbox("Region",['Southwest', 'Southeast', 'Northwest', 'Northeast'])
    user_region=data['encode']['region'].transform([[user_region.lower()]]).flatten().tolist()


    button=st.button("Predict")
    

if button:
    val=[[age,sex,bmi,children,smoker]+user_region]
    scaled=data['scaler'].transform(val)
    pred=data['model'].predict(scaled)[0]
    if pred>0:
        st.success(f"Predicted Price(Charge) in $:  {round(pred,2)} ")
    else:
        st.sucess(f'Predicted Charge is 0')