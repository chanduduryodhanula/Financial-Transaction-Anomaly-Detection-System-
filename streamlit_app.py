import streamlit as st
import joblib
import pandas as pd
from PIL import Image
from pymongo import MongoClient

# Connect to MongoDB
uri = "mongodb+srv://70020052:<password>@cluster1.6osp93a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client = MongoClient(uri)
db = client.get_database("AnomalyDetection")
Credit_Card_Defaulter = db.Defaulter_Prediction

# Load Isolation Forest model
model = joblib.load('isolation_forest_model.pkl')

# Define feature options
transaction_types = ['Purchase', 'Transfer', 'Withdrawal']
locations = ['London', 'Los Angeles', 'New York', 'San Francisco', 'Tokyo']
account_ids = ['ACC1', 'ACC10', 'ACC11', 'ACC12', 'ACC13', 
               'ACC14', 'ACC15', 'ACC2', 'ACC3', 'ACC4', 
               'ACC5', 'ACC6', 'ACC7', 'ACC8', 'ACC9']
merchant_types = ['MerchantA', 'MerchantB', 'MerchantC', 'MerchantD', 
                  'MerchantE', 'MerchantF', 'MerchantG', 'MerchantH', 
                  'MerchantI', 'MerchantJ']

# Streamlit app layout
st.markdown('Author: @OnkarSudrik')
st.title('Anomaly Detection with Isolation Forest Model')
st.markdown(
    """
    Detect anomalies in transactions using an Isolation Forest model. Fill in the details below and click 'Predict Anomaly' to predict whether it's a fishy transaction or not.
    """
)

# Load and display an image
#image = Image.open('C:\\Users\\LENOVO\\Downloads\\outlier-smaller.webp')
#st.image(image, caption='', use_column_width=True)

# Input fields
col1, col2 = st.columns([1, 2])
with col1:
    amount = st.number_input('Amount (Dollars)', min_value=0.0, step=0.01)
with col2:
    transaction_type = st.selectbox('Transaction Type', transaction_types)
    location = st.selectbox('Location', locations)
    account_id = st.selectbox('Account ID', account_ids)
    merchant_type = st.selectbox('Merchant Type', merchant_types)

# Prediction button
col1, col2 = st.columns([2, 1])
with col1:
    st.write('')
with col2:
    if st.button('Predict Anomaly'):
        # Prepare input data for prediction
        input_data = {
            'Amount': [amount],
            'TransactionType_Purchase': [1 if transaction_type == 'Purchase' else 0],
            'TransactionType_Transfer': [1 if transaction_type == 'Transfer' else 0],
            'TransactionType_Withdrawal': [1 if transaction_type == 'Withdrawal' else 0],
            'Location_London': [1 if location == 'London' else 0],
            'Location_Los Angeles': [1 if location == 'Los Angeles' else 0],
            'Location_New York': [1 if location == 'New York' else 0],
            'Location_San Francisco': [1 if location == 'San Francisco' else 0],
            'Location_Tokyo': [1 if location == 'Tokyo' else 0],

            'AccountID_ACC1': [1 if account_id == 'ACC1' else 0],
            'AccountID_ACC10': [1 if account_id == 'ACC10' else 0],
            'AccountID_ACC11': [1 if account_id == 'ACC11' else 0],
            'AccountID_ACC12': [1 if account_id == 'ACC12' else 0],
            'AccountID_ACC13': [1 if account_id == 'ACC13' else 0],
            'AccountID_ACC14': [1 if account_id == 'ACC14' else 0],
            'AccountID_ACC15': [1 if account_id == 'ACC15' else 0],
            'AccountID_ACC2': [1 if account_id == 'ACC2' else 0],
            'AccountID_ACC3': [1 if account_id == 'ACC3' else 0],
            'AccountID_ACC4': [1 if account_id == 'ACC4' else 0],
            'AccountID_ACC5': [1 if account_id == 'ACC5' else 0],
            'AccountID_ACC6': [1 if account_id == 'ACC6' else 0],
            'AccountID_ACC7': [1 if account_id == 'ACC7' else 0],
            'AccountID_ACC8': [1 if account_id == 'ACC8' else 0],
            'AccountID_ACC9': [1 if account_id == 'ACC9' else 0],

            'Merchant_MerchantA': [1 if merchant_type == 'MerchantA' else 0],
            'Merchant_MerchantB': [1 if merchant_type == 'MerchantB' else 0],
            'Merchant_MerchantC': [1 if merchant_type == 'MerchantC' else 0],
            'Merchant_MerchantD': [1 if merchant_type == 'MerchantD' else 0],
            'Merchant_MerchantE': [1 if merchant_type == 'MerchantE' else 0],
            'Merchant_MerchantF': [1 if merchant_type == 'MerchantF' else 0],
            'Merchant_MerchantG': [1 if merchant_type == 'MerchantG' else 0],
            'Merchant_MerchantH': [1 if merchant_type == 'MerchantH' else 0],
            'Merchant_MerchantI': [1 if merchant_type == 'MerchantI' else 0],
            'Merchant_MerchantJ': [1 if merchant_type == 'MerchantJ' else 0]
        }

        # Convert input data to DataFrame
        input_df = pd.DataFrame(input_data)

        # Make prediction
        prediction = model.predict(input_df)

        # Store input data along with prediction in MongoDB collection
        data_to_insert = {
            'Amount': amount,
            'TransactionType': transaction_type,
            'Location': location,
            'AccountID': account_id,
            'MerchantType': merchant_type,
            'Prediction': 'Normal' if prediction[0] == 1 else 'Anomaly'
        }

        # Insert data into MongoDB collection
        Credit_Card_Defaulter.insert_one(data_to_insert)

        # Display prediction with styled result
        if prediction[0] == 1:
            st.success('Prediction: This seems to be a normal Transaction')
        else:
            st.error('Prediction: This could be a fishy Transaction')
