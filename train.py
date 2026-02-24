import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# ... (data loading and preprocessing code) ...
spending_habits = pd.read_csv("customer_spend_regression.csv")
X = spending_habits.drop(columns = ['MonthlySpend'])
y = spending_habits['MonthlySpend']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestRegressor(criterion = 'absolute_error',
                               n_estimators = 1000, 
                               max_features = 'sqrt',  
                               max_depth = 10,
                               min_samples_split = 2,
                               min_samples_leaf = 1,
                               bootstrap = True)
model.fit(X_train, y_train)

path = r'artifacts\\random_forest.sav'
joblib.dump(model, path)
print("Model Artifact Created!")