📉 Customer Churn Prediction using XGBoost
This project aims to predict customer churn using machine learning, specifically the XGBoost classifier. The model is trained on a telecom dataset and deployed using a user-friendly Streamlit web app for interactive usage.

🔍 Problem Statement
Customer churn is a critical metric for businesses in competitive markets. Predicting churn in advance enables companies to take proactive measures to retain customers and reduce losses. This project builds a churn prediction model using historical customer data.

🚀 Features
📊 Data preprocessing and feature engineering

⚙️ Model training using XGBoost

📈 Performance evaluation with accuracy, confusion matrix, and classification report

🌐 Interactive Streamlit web app for real-time predictions

📁 Upload your own CSV file or input data manually

📦 Tech Stack
Python

pandas, NumPy

XGBoost

Scikit-learn

Matplotlib, Seaborn

Streamlit

🧠 Model
Algorithm Used: XGBoost Classifier

Evaluation Metrics:

Accuracy

Precision / Recall / F1-score

Confusion Matrix

Input Features: Customer demographics, tenure, usage metrics, service subscriptions, etc.

🧪 How to Run Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/kishore-1808/churnprediction
cd customer-churn-prediction
Create a virtual environment and install dependencies:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app/churn_app.py
🖥️ Live Demo
If deployed, add your link below:

🌐 Try the Live App

📊 Sample Inputs for Prediction
Feature	Example Value
Gender	Female
SeniorCitizen	0
Partner	Yes
MonthlyCharges	70.35
TotalCharges	1397.475
...	...
