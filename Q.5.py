import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score

df = pd.read_csv("filled_test.csv", header="infer")

df['Loan_Status'] = (df['Credit_History'] > 0).astype(int) 
df = df.dropna(subset=['Loan_Status'])

# 3. Convert categorical → numerical
# Binary encoding
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Married'] = df['Married'].map({'Yes': 1, 'No': 0})
df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
df['Self_Employed'] = df['Self_Employed'].map({'Yes': 1, 'No': 0})
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

# Dependents column fix (3+ → 3)
df['Dependents'] = df['Dependents'].replace('3+', 3).astype(int)

# One-hot encoding for Property_Area
df = pd.get_dummies(df, columns=['Property_Area'], drop_first=True)

X = df.drop(columns=['Loan_Status', 'Credit_History', 'Loan_ID'])
y = df['Loan_Status'] 

print(df.head())

# -----------------------------
# 1. Split data (80% train, 20% test)
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 2. Train KNN model
# -----------------------------
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# -----------------------------
# 3. Make predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 4. Evaluate model
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# -----------------------------
# 5. Print results
# -----------------------------
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)