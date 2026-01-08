import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
import joblib
import pickle


df = pd.read_csv("D:\\Project\\new_projects\\AD\\financial_anomaly_data.csv") 

# Rename columns
df.rename(columns={'TransactionID_Suffix': 'TransactionID', 
                   'AccountID_Suffix': 'AccountID', 
                   'Merchant_Suffix': 'Merchant'}, inplace=True)

null_values = df.isnull().sum() 

df['Amount'].fillna(df['Amount'].mean(), inplace=True)

for column in ['TransactionType', 'Location', 'Timestamp','TransactionID', 'AccountID', 'Merchant']:
    df[column].fillna(df[column].mode()[0], inplace=True) 

    df.isnull().sum() 


# List of categorical features
categorical_features = ['TransactionType', 'Location', 'AccountID', 'Merchant']

# Perform one-hot encoding
df = pd.get_dummies(df, columns=categorical_features)

# Drop the 'TransactionID' column
df.drop(columns=['TransactionID','Timestamp'], inplace=True)

# MODEL Building 

# Exclude 'Amount' from the features
X = df

# Split the data into training and testing sets
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Initialize and train the Isolation Forest model
model = IsolationForest(contamination=0.02, random_state=42)  # Adjust contamination parameter as needed
model.fit(X_train)

# Predict anomalies on the testing set
y_pred = model.predict(X_test)

# Assuming y_pred contains the predicted labels
unique_labels, counts = np.unique(y_pred, return_counts=True)



# Specify the file path where you want to save the model
model_file_path = 'isolation_forest_model.pkl'

# Save the model to the specified file path
pickle.dump(model, open(model_file_path,'wb'))