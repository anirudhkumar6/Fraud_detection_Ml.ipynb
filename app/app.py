import streamlit as st 
import pandas as pd
import joblib
import os

# 🚀 Fraud Detection Prediction Model (Streamlit Frontend)
# - Loads trained model from 'Model/fraud_detection_model.pkl'
# - Provides UI for entering transaction details
# - Predicts fraud (1) or non-fraud (0)

st.title('Fraud Detection Prediction Model')

Model_path = os.path.join("Model","fraud_detection_model.pkl")
model = joblib.load(Model_path)


st.markdown('Please enter the following detailes and use the predict button')
st.divider()

# 📝 Input fields for transaction details


transaction_type = st.selectbox('Transaction Type', ['CASH_OUT', 'PAYMENT', 'TRANSFER', 'DEPOSIT'])
amount = st.number_input('Amount', min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input('Old Balance (Sender)', min_value =0.0, value=0.0)
newbalanceOrig = st.number_input('New Balance (Sender)', min_value=0.0, value=0.0)
oldbalanceDest = st.number_input('Old Balance (Receiver)', min_value=0.0, value=0.0)
newbalanceDest = st.number_input('New Balance (Receiver)', min_value=0.0, value=0.0)

# 🔮 Prediction button


if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type" : transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
        }])
    

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction == 1:
        st.error('The transaction is Fraud')
    else:
        st.success('The transaction is Not fraud')