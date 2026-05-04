# DAY 4 + DAY 5 - ML MODEL

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load Dataset
df = pd.read_csv(r"C:\Users\KIIT\Churn-Prediction-ML\data\Churn(1).csv")

# 2. Data Cleaning
# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing values
df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].mean()
)

# 3. Drop Unnecessary Column\
df.drop("customerID", axis=1, inplace=True)

# 4. Convert Yes/No -> 1/0
yes_no_cols = [
    "Partner",
    "Dependents",
    "PhoneService",
    "PaperlessBilling",
    "Churn"
]

for col in yes_no_cols:
    df[col] = df[col].map({
        "Yes": 1,
        "No": 0
    })

# 5. One-Hot Encoding
df = pd.get_dummies(
    df,
    drop_first=True
)

# Remove remaining missing values
df = df.fillna(0)

# 6. Features and Target
X = df.drop("Churn", axis=1)

y = df["Churn"]

# 7. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 8. Train Model
model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train, y_train)

# 9. Prediction
y_pred = model.predict(X_test)

# 10. Accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)
print("Model Accuracy:", accuracy)