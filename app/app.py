# 1 is good (lower risk)
# 0 is bad (higher risk)

import streamlit as st
import pandas as pd
import joblib 
import os

#Loading Model & encoders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENCODERS_DIR = os.path.join(BASE_DIR, "..", "encoders")

cols = ["Sex", "Housing", "Saving accounts", "Checking account"]

encoders = {
    col: joblib.load(os.path.join(ENCODERS_DIR, f"{col}_encoder.pkl"))
    for col in cols
}

# buliding the form 
st.title('Credit Risk Prediction App')
st.write('enter your application information to predict')        
age = st.number_input('Age',min_value=18,max_value=80,value=30)
sex = st.selectbox("Sex", ["male","female"])
job = st.number_input("Job (0-3)", min_value = 0, max_value= 3, value = 1)
housing = st.selectbox("Housing", ["own","rent","free"])
Saving_accounts=st.selectbox("Saving Accounts", ["little", "moderate", "rich","quite rich"])
Checking_account=st.selectbox("Checking Account", ["little", "moderate", "rich"])
credit_amount = st.number_input('Credit Amount',min_value=0,value=1000)
duration=st.number_input("Duration {months}", min_value=1, value=12)

#Makeing data fram for model
input_df = pd.DataFrame({
    "Age": [age],
    "Sex": [encoders["Sex"].transform([sex])[0]],
    "Job": [job],
    "Housing": [encoders["Housing"].transform([housing])[0]],
    "Saving accounts": [encoders["Saving accounts"].transform([Saving_accounts])[0]],
    "Checking account": [encoders["Checking account"].transform([Checking_account])[0]],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})


if st.button('Predicct Risk'):
    pred=model.predict(input_df)[0]

    if pred == 1:
        st.success('The Predicted ctedit risk is **GOOD**')
    else:
        st.error('The Predicted ctedit risk is **BAD**')


