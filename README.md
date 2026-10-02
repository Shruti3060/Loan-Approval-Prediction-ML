# Loan Approval Prediction using Machine Learning

A Machine Learning project that predicts whether a loan application is likely to be approved or rejected based on applicant and financial information.

The project uses a Logistic Regression model trained on historical loan application data and provides a user-friendly web interface using Streamlit.

---

## Project Overview

Loan approval decisions depend on several factors such as income, loan amount, CIBIL score, loan term, education, employment status, and asset values.

This project uses Machine Learning to analyze these applicant details and predict the loan approval status.

The trained model is integrated with a Streamlit web application so users can enter applicant information and receive a prediction.

---

## Objectives

The main objectives of this project are:

- Analyze historical loan application data
- Perform data cleaning and preprocessing
- Identify relevant features for loan prediction
- Train a Machine Learning classification model
- Evaluate the model's performance
- Predict loan approval status for new applicants
- Develop a simple interactive web application
- Deploy the application for online access

---

## 📊 Dataset

The dataset contains **4,269 loan application records** and **12 input features**.

### Features Used

| Feature | Description |
|---|---|
| Loan ID | Unique identification number of the loan |
| Number of Dependents | Number of dependents of the applicant |
| Education | Applicant's education status |
| Self Employed | Whether the applicant is self-employed |
| Annual Income | Applicant's annual income |
| Loan Amount | Requested loan amount |
| Loan Term | Loan repayment period |
| CIBIL Score | Applicant's credit score |
| Residential Assets Value | Value of residential assets |
| Commercial Assets Value | Value of commercial assets |
| Luxury Assets Value | Value of luxury assets |
| Bank Asset Value | Value of bank assets |

### Target

**Loan Status**

The model predicts the loan application status based on the above features.

---

## Project Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Data Preprocessing
     ↓
Feature Selection
     ↓
Train-Test Split
     ↓
Logistic Regression
     ↓
Model Evaluation
     ↓
Save Trained Model
     ↓
Streamlit Web Application
     ↓
Loan Prediction

##  Live Demo

Try the deployed Loan Approval Prediction application:

[Loan Approval Predictor](https://loan-approval-prediction-ml-fynm7n4ycpiqptrl7keiky.streamlit.app/)


