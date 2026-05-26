import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# LOAD DATASET
data = pd.read_csv("creditcard.csv/creditcard.csv")


# DISPLAY DATA
print("\nFirst 5 Rows:\n")
print(data.head())

print("\nDataset Information:\n")
print(data.info())

print("\nFraud vs Genuine Transactions:\n")
print(data['Class'].value_counts())


# FEATURES AND TARGET
X = data[['Amount']]

y = data['Class']


# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# TRAIN MODEL
print("\nTraining Random Forest Model...\n")

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)


# PREDICTION
rf_pred = rf_model.predict(X_test)


# ACCURACY
accuracy = accuracy_score(y_test, rf_pred)

print("\nModel Accuracy:\n")
print(accuracy)


# CLASSIFICATION REPORT
print("\nClassification Report:\n")
print(classification_report(y_test, rf_pred))


# CONFUSION MATRIX
cm = confusion_matrix(y_test, rf_pred)

plt.figure(figsize=(6,4))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig("confusion_matrix.png")


# SAVE MODEL
joblib.dump(rf_model, "fraud_model.pkl")

print("\nModel saved successfully!")