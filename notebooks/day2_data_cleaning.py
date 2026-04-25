# DAY 2 - DATA CLEANING

import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\KIIT\Churn-Prediction-ML\data\Churn(1).csv")

# 1. Fix TotalCharges column

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# 2. Check missing values

print(df.isnull().sum())

# 3. Handle missing values

df["TotalCharges"].fillna(df["TotalCharges"].mean(), inplace=True)

# 4. Convert target column (Churn) to numbers

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# 5. Convert binary columns (Yes/No → 1/0)

binary_cols = ["Partner", "Dependents", "PhoneService", "PaperlessBilling"]

for col in binary_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0})

# 6. Check final data

print(df.info())
print(df.head())