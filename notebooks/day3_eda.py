# DAY 3 - EDA (Visualization)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\KIIT\Churn-Prediction-ML\data\Churn(1).csv")

# Fix TotalCharges
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"].fillna(df["TotalCharges"].mean(), inplace=True)

# Convert Churn to numeric
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# 1. Churn Distribution

sns.countplot(x="Churn", data=df)
plt.title("Churn Distribution")
plt.show()

# 2. Gender vs Churn

sns.countplot(x="gender", hue="Churn", data=df)
plt.title("Gender vs Churn")
plt.show()

# 3. Contract Type vs Churn

sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Contract Type vs Churn")
plt.xticks(rotation=20)
plt.show()

# 4. Monthly Charges Distribution

plt.hist(df["MonthlyCharges"], bins=30)
plt.title("Monthly Charges Distribution")
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.show()

# 5. Tenure vs Churn

sns.boxplot(x="Churn", y="tenure", data=df)
plt.title("Tenure vs Churn")
plt.show()