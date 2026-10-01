import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("loan_approval_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)

# Title
st.title("🏦 Loan Approval Predictor")
st.write("Enter applicant details to predict loan approval.")

st.divider()

# Input fields
loan_id = st.number_input("Loan ID", min_value=1, value=1)

no_of_dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=20,
    value=2
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["No", "Yes"]
)

income_annum = st.number_input(
    "Annual Income",
    min_value=0,
    value=5000000,
    step=100000
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=15000000,
    step=100000
)

loan_term = st.number_input(
    "Loan Term (Years)",
    min_value=1,
    max_value=50,
    value=15
)

cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900,
    value=780
)

residential_assets_value = st.number_input(
    "Residential Assets Value",
    min_value=0,
    value=5000000,
    step=100000
)

commercial_assets_value = st.number_input(
    "Commercial Assets Value",
    min_value=0,
    value=2000000,
    step=100000
)

luxury_assets_value = st.number_input(
    "Luxury Assets Value",
    min_value=0,
    value=8000000,
    step=100000
)

bank_asset_value = st.number_input(
    "Bank Asset Value",
    min_value=0,
    value=4000000,
    step=100000
)

st.divider()

# Prediction button
if st.button("🔮 PREDICT LOAN", use_container_width=True):

    # Convert categorical values into the same format used during training
    education_value = 1 if education == "Graduate" else 0
    self_employed_value = 1 if self_employed == "Yes" else 0

    # Create input DataFrame
    new_applicant = pd.DataFrame([[
        loan_id,
        no_of_dependents,
        education_value,
        self_employed_value,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value
    ]], columns=[
        "loan_id",
        "no_of_dependents",
        "education",
        "self_employed",
        "income_annum",
        "loan_amount",
        "loan_term",
        "cibil_score",
        "residential_assets_value",
        "commercial_assets_value",
        "luxury_assets_value",
        "bank_asset_value"
    ])

    # Prediction
    prediction = model.predict(new_applicant)[0]

    # Probability
    probability = model.predict_proba(new_applicant)[0][1] * 100

    # Display result
    if prediction == 1:
        st.success("✅ LOAN APPROVED")
        st.metric("Approval Probability", f"{probability:.2f}%")
    else:
        st.error("❌ LOAN REJECTED")
        st.metric("Approval Probability", f"{probability:.2f}%")