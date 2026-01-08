# Financial Transaction Anomaly Detection System

## 📌 Overview
Financial institutions handle thousands of transactions every day, and some of them may be unusual or risky.  
This project focuses on **detecting abnormal financial transactions** using machine learning techniques.

The system helps identify transactions that do not follow normal patterns, which can support fraud detection and risk monitoring.

---

## 🎯 Objective
- Detect unusual or suspicious financial transactions  
- Analyze transaction patterns using historical data  
- Provide a simple interface to check whether a transaction is normal or anomalous  

---

## 🛠 Tools & Technologies
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Machine Learning Models:**
  - Isolation Forest  
  - Local Outlier Factor (LOF)  
- **Web Framework:** Streamlit  
- **Database:** MongoDB (optional integration)

---

## 🔍 Project Workflow
1. Performed exploratory data analysis (EDA) to understand transaction behavior  
2. Cleaned and prepared transaction data for modeling  
3. Trained anomaly detection models using unsupervised learning  
4. Evaluated model results to identify abnormal transactions  
5. Built a Streamlit web app for real-time anomaly prediction  

---

## 📊 Models Used
- **Isolation Forest:** Used as the primary model to detect anomalies efficiently  
- **Local Outlier Factor (LOF):** Used to compare and validate anomaly patterns  

Both models work without labeled data, making them suitable for real-world financial scenarios.

---

## 🖥 User Interface
The Streamlit web application allows users to:
- Enter transaction details  
- Instantly check whether a transaction is normal or anomalous  

---

## 📁 Project Files
├── Eda_AnomalyDetection.ipynb # Exploratory data analysis
├── model.py # Model training and prediction logic
├── streamlit_app.py # Web application
├── financial_anomaly_data.csv # Dataset
├── requirements.txt # Dependencies

---

## 🚀 Future Improvements
- Improve model accuracy with additional features  
- Add visual dashboards for transaction monitoring  
- Deploy the application on cloud platforms  

---

## 👤 Author
Chandu Duryodhanula  
Aspiring Machine Learning Engineer


