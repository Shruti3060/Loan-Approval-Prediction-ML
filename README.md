# Loan Approval Prediction using Machine Learning

## 📌 Project Overview

This project uses Machine Learning to predict whether a loan application will be approved or rejected based on applicant and financial information.

The project uses a Logistic Regression model trained on historical loan application data.

## 🎯 Objective

To build a Machine Learning model that can:

- Analyze loan applicant information
- Predict loan approval status
- Evaluate model performance
- Generate predictions for new applicants

## 📊 Dataset

- Total records: 4,269
- Input features: 12
- Target: Loan Status

### Features Used

- Loan ID
- Number of Dependents
- Education
- Self Employed
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Assets Value
- Commercial Assets Value
- Luxury Assets Value
- Bank Asset Value

## 🤖 Machine Learning Model

**Logistic Regression**

The dataset was divided into training and testing sets before training the model.

## 📈 Model Performance

**Accuracy: 82.32%**

The model was evaluated using:

- Accuracy
- Confusion Matrix
- Classification Report
- Precision
- Recall
- F1-Score

## 🔮 Prediction Example

The trained model was tested with new loan applicants.

Example results:

| Applicant | Prediction | Approval Probability |
|-----------|------------|----------------------|
| Applicant 1 | Approved ✅ | 94.71% |
| Applicant 2 | Approved ✅ | 76.01% |
| Applicant 3 | Approved ✅ | 96.09% |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Jupyter Notebook

## 📁 Project Structure

```text
Loan_Approval_Project/
│
├── Loan_Approval.ipynb
├── loan_approval_dataset.csv
├── cleaned_loan_dataset.csv
├── loan_approval_model.pkl
├── requirements.txt
└── README.md