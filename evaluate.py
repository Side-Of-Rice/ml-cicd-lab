import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score
from prettytable import PrettyTable
import joblib
import os

# Define the file path
file_path = r'artifacts\\random_forest.sav'

# Load the artifact from the file
try:
    with open(file_path, 'rb') as file:
        loaded_object = joblib.load(file_path)
    print("Artifact loaded successfully!")
    
    # You can now use the loaded_object in your code
    spending_habits = pd.read_csv("customer_spend_regression.csv")
    X = spending_habits.drop(columns = ['MonthlySpend'])
    y = spending_habits['MonthlySpend']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    y_pred = loaded_object.predict(X_test)
    
    rmse = root_mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    #Intentionally Fail
    r2 = 0.2

    Performance_Metric = PrettyTable(["RMSE", "MAE", "R^2"])
    Performance_Metric.add_row([rmse, mae, r2])

    print(Performance_Metric)
    
    with open('r2 score.txt', 'w') as f:
        f.write(str(r2))
    
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred during loading: {e}")

