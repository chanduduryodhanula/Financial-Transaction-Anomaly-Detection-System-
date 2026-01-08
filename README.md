# Anomaly-Detection-System

Anomaly Detection System: Predicts anomalies in financial transactions using Isolation Forest model. Includes exploratory data analysis (EDA), model selection, model evaluation, model training, MongoDB integration for data storage, and deployment using Streamlit web app.

## Overview
This project focuses on detecting anomalies in financial transactions using machine learning techniques. It encompasses various stages such as exploratory data analysis (EDA), model building, and deployment of a Streamlit web application for predicting anomalies in real-time.

## Files
- **model.py**: Contains files for model building, training, and saving.
- **Isolation_forest_model.pkl**: Saved model file.
- **streamlit_app.py**: Web application file with MongoDB connection.
- **Eda_AnomalyDetection.ipynb**: Jupyter Notebook file for exploratory data analysis.
- **Requiremets.txt**: Requirements file specifying the dependencies.

## Dataset Information
The dataset contains information on financial transactions, including timestamps, transaction IDs, account IDs, transaction amounts, merchant details, transaction types, and locations.

## Technical Aspect
The project can be broken down into the following components:
1. **Model Building**:
   - Utilizes the Isolation Forest algorithm for anomaly detection.
   - Includes feature engineering, one-hot encoding, and model training.
2. **Streamlit Web Application**:
   - Development using Streamlit for interactive user interface.
   - Integration with MongoDB for storing transaction data and predictions.
   - Deployment on a local server for real-time predictions.

## User Interface
The web application provides a user-friendly interface for users to input transaction details and receive predictions regarding whether the transaction is an anomaly or not.

## Technologies Used

[<img target="_blank" src="https://www.python.org/static/img/python-logo.png" width=100 style="margin-right: 20px;">](https://www.python.org/)    [<img target="_blank" src="https://pandas.pydata.org/static/img/pandas_mark.svg" width=100 style="margin-right: 20px;">](https://pandas.pydata.org/)    [<img target="_blank" src="https://numpy.org/images/logo.svg" width=100 style="margin-right: 20px;">](https://numpy.org/)    [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width=100 style="margin-right: 20px;">](https://scikit-learn.org/stable/)    [<img target="_blank" src="https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width=100 style="margin-right: 20px;">](https://www.streamlit.io/)    [<img target="_blank" src="https://www.mongodb.com/assets/images/global/favicon.ico" width=100 style="margin-right: 20px;">](https://www.mongodb.com/)    [<img target="_blank" src="https://user-images.githubusercontent.com/315810/92159303-30d41100-edfb-11ea-8107-1c5352202571.png" width=100 style="margin-right: 20px;">](https://matplotlib.org/)

## Things to Remember

This web application in streamlit_app.py file will not collect your data unless you edit the MongoDB connection according to your needs in the following lines of code:

```python
# Connect to MongoDB
uri = "mongodb+srv://70020052:<password>@cluster1.6osp93a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client = MongoClient(uri)
db = client.get_database("Your_Database_name")
Credit_Card_Defaulter = db.Your_collection_name
```
This section provides clear instructions on how to customize the MongoDB connection parameters to suit individual needs.

## Installation
Ensure you have Python 3.x installed. Clone the repository and navigate to the project directory. Create a virtual environment and install the required packages using:
```bash
pip install -r requirements.txt 
```


