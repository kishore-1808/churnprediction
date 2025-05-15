import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("xgboost_model.pkl")  # Update with correct file if needed
scaler = joblib.load("scaler.pkl")        # Make sure you saved your StandardScaler too

# Title
st.title("📉 Customer Churn Prediction App")

# Input form
with st.form("churn_form"):
    CreditScore = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
    Geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", min_value=18, max_value=100, value=40)
    Tenure = st.slider("Tenure", 0, 10, 3)
    Balance = st.number_input("Balance", value=100000.0)
    NumOfProducts = st.selectbox("Number of Products", [1, 2, 3, 4])
    HasCrCard = st.selectbox("Has Credit Card", [1, 0])
    IsActiveMember = st.selectbox("Is Active Member", [1, 0])
    EstimatedSalary = st.number_input("Estimated Salary", value=50000.0)
    
    submitted = st.form_submit_button("Predict")

if submitted:
    # Encode categorical values
    gender_encoded = 1 if Gender == "Male" else 0
    geography_map = {"France": 0, "Spain": 1, "Germany": 2}
    geo_encoded = geography_map[Geography]

    # Create input DataFrame
    input_data = pd.DataFrame([[
        CreditScore, geo_encoded, gender_encoded, Age, Tenure, Balance,
        NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary
    ]], columns=[
        'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance',
        'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary'
    ])

    # Scale features
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    # Display result
    if prediction == 1:
        st.error(f"❌ Customer likely to churn (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer likely to stay (Probability: {prob:.2f})")
