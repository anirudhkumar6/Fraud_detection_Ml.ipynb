# 🚨 Fraud Detection System using Machine Learning

## 📖 Project Overview

This project is a **machine learning–based fraud detection system** developed as a **learning and practice project** to understand how real-world financial fraud detection systems work.

The model analyzes transaction details such as **transaction type, transaction amount, and account balances** to predict whether a transaction is **fraudulent or legitimate**.

### 🔹 Project Focus Areas

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Pipelines
- Basic model deployment using **Streamlit**

⚠️ **Note:** This is a **prototype / learning project**, not a production-ready system.

---

## 📑 Table of Contents

- [📖 Project Overview](#-project-overview)
- [📊 Dataset Information](#-dataset-information)
- [🧩 Features Used for Prediction](#-features-used-for-prediction)
- [🗂️ Project Structure](#️-project-structure)
- [🔄 Machine Learning Workflow](#-machine-learning-workflow)
- [🤖 Model Details](#-model-details)
- [📈 Model Performance](#-model-performance)
- [⚠️ Important Limitations](#️-important-limitations)
- [🖥️ Web Application](#️-web-application)
- [▶️ How to Run the Project](#️-how-to-run-the-project)
- [🛠️ Technologies & Libraries Used](#️-technologies--libraries-used)
- [🚀 Future Improvements](#-future-improvements)
- [👤 Author & Contact](#-author--contact)

---

## 📊 Dataset Information

- **Source:** Kaggle (Synthetic Financial Transactions Dataset)
- **File Format:** CSV
- **Dataset Size:** ~6.3 million transactions
- **Fraud Ratio:** ~0.12% (Highly imbalanced dataset)
- **Target Column:** `isFraud`

---

## 🧩 Features Used for Prediction

- Transaction Type  
- Transaction Amount  
- Old Balance (Sender)  
- New Balance (Sender)  
- Old Balance (Receiver)  
- New Balance (Receiver)  
- Balance Difference (Sender)  
- Balance Difference (Receiver)

🔹 **Additional engineered features** were created to capture suspicious balance changes, which play a key role in fraud detection.

---

## 🗂️ Project Structure

```text
fraud_detection_project/
│
├── data/
│   └── fraud_data.csv          # Dataset file
│
├── notebook/
│   └── FD_model.ipynb          # EDA, feature engineering & model training
│
├── model/
│   └── fraud_model.pkl         # Trained ML pipeline (Joblib)
│
├── app/
│   └── app.py                  # Streamlit-based web application
│
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## 🔄 Machine Learning Workflow

- Data loading and inspection  
- Exploratory Data Analysis (EDA)  
- Data cleaning 
- Data visualization  
  - Histograms  
  - Box plots  
  - Correlation heatmap  
- Feature engineering  
  - Balance difference calculations  
- Categorical encoding
- Model training using a pipeline  
- Model evaluation  
- Model saving using **Joblib**

---

## 🤖 Model Details

- **Algorithm Used:** Logistic Regression  

### 🔍 Why Logistic Regression?

- Simple and interpretable  
- Strong baseline for classification problems  
- Suitable for learning ML fundamentals  

### ⚖️ Class Imbalance Handling

- Used `class_weight='balanced'` to address extreme class imbalance  

### 📏 Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  

⚠️ This model is a **baseline prototype**, not optimized for production use.

---

## 📈 Model Performance

- **Accuracy:** ~94.6%  
- **F1-Score (Fraud Class):** Low due to extreme class imbalance  
- **Recall (Fraud Class):** Needs improvement  

---

## ⚠️ Important Limitations

Due to the **highly imbalanced dataset**, the model may:

- Miss some fraud cases  
- Incorrectly classify certain transaction types (e.g., **TRANSFER**, **CASH_OUT**)  

These limitations are **acknowledged** and planned to be improved in future versions.

---

## 🖥️ Web Application

- **Framework:** Streamlit  

### 🔧 Functionality

- User enters transaction details  
- Model predicts whether the transaction is:  
  - **Fraudulent (1)**  
  - **Legitimate (0)**  

- **Deployment Type:** Local  

📌 The app runs on a local machine and stops when the system or IDE is closed.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone <https://github.com/anirudhkumar6/Fraud_detection-_Ml.ipynb.git>
cd fraud_detection_project 
```

### 2️⃣ Install Dependencies

 ```bash
  pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app/app.py
```

---

## 🛠️ Technologies & Libraries Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn
- OS
- Warnings

---

## 🚀 Future Improvements

- ### This project is a learning prototype, and future enhancements may include

1. Trying advanced models (Random Forest, XGBoost, Knn, etc...)
2. Improving Recall and F1-Score for fraud class
3. Better handling of extreme class imbalance
4. Real-time transaction processing
5. REST API using FastAPI
6. Cloud deployment
7. Model explainability (SHAP, feature importance)
8. Building a production-level fraud detection system over time

---

## 👤 Author & Contact

### Name: Anirudh Kumar

#### 📧 Email: *<anirudhkumar79030@gmail.com>*

#### 🔗 LinkedIn: *<https://www.linkedin.com/in/anirudhkumar6>*
