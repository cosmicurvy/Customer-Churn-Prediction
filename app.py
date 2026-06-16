import streamlit as st
import pandas as pd
from src.pipeline import load_artifacts, predict_churn

#loading the artifacts
@st.cache_resource
def get_assets():
    return load_artifacts()

encoder, model = get_assets()

# streamlit UI
st.set_page_config("Customer Churn Prediction", layout='centered')
st.title("Customer Churn Prediction App")
st.write("Enter customer details to predict churn probability.")

# user input
gender = st.selectbox("Gender", ['Male','Female'])
Partner = st.selectbox("Partner", ['Yes', 'No'])
Dependents = st.selectbox("Dependents", ['Yes', 'No'])
PhoneService = st.selectbox("PhoneService", ['Yes', 'No'])
MultipleLines = st.selectbox("MultipleLines", ['Yes', 'No'])
InternetService = st.selectbox("InternetService", ['DSL','Fiber optic','No'])
OnlineSecurity  = st.selectbox("OnlineSecurity", ['Yes', 'No'])
OnlineBackup = st.selectbox("OnlineBackup", ['Yes', 'No'])
DeviceProtection = st.selectbox("DeviceProtection", ['Yes', 'No'])
TechSupport = st.selectbox("TechSupport", ['Yes', 'No'])
StreamingTV = st.selectbox("StreamingTV", ['Yes', 'No'])
StreamingMovies = st.selectbox("StreamingMovies", ['Yes', 'No'])
Contract = st.selectbox("Contract", ['Month-to-month','One year','Two year'])
PaperlessBilling = st.selectbox("PaperlessBilling", ['Yes', 'No'])
PaymentMethod = st.selectbox("PaymentMethod", ['Electronic check','Mailed check','Bank transfer','Credit card'])
tenure = st.number_input("Tenure (months)", min_value=0.0, max_value=100.0)
MonthlyCharges = st.number_input("MonthlyCharges", min_value=10.0, max_value=200.0)
SeniorCitizen = st.selectbox("Are you a Senior Citizen?(1 for yes)", [1, 0])

#create data frame
input_data = pd.DataFrame({
    'gender' : [gender], 'SeniorCitizen' : [SeniorCitizen], 'Partner' : [Partner],
    'Dependents' : [Dependents], 'tenure' : [tenure],'PhoneService' : [PhoneService],
    'MultipleLines' : [MultipleLines], 'InternetService' : [InternetService],
    'OnlineSecurity' : [OnlineSecurity], 'OnlineBackup' : [OnlineBackup],
    'DeviceProtection' : [DeviceProtection], 'TechSupport' : [TechSupport],
    'StreamingTV' : [StreamingTV], 'StreamingMovies' : [StreamingMovies],
    'Contract' : [Contract], 'PaperlessBilling' : [PaperlessBilling],
    'PaymentMethod' : [PaymentMethod], 'MonthlyCharges' : [MonthlyCharges]
})


if st.button("Predict Churn"):
    prediction, probability = predict_churn(input_data=input_data, encoder=encoder, model=model)

    if prediction == 1:
        st.error(f"Customer is likely to churn (Probability: {probability:.2f})")
    else:
        st.success(f"Customer is likely to stay (Probability: {probability:.2f})")