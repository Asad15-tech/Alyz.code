import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Reading the data...")
data = pd.read_csv('heart_disease_uci.csv')

print("Preparing features and target...")
X = data.drop('target', axis=1)
y = data['target']

print("Splitting the data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training the model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Saving the model with joblib...")
joblib.dump(model, 'new_heart_model.joblib')
print("Model saved successfully!")

# Test the model
test_score = model.score(X_test, y_test)
print(f"\nModel accuracy on test data: {test_score:.2%}")