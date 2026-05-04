# 🚀 Customer Churn Prediction ML Project

## 📌 Overview
This project focuses on analyzing customer churn data and predicting whether a customer is likely to leave the company using Machine Learning.

The project covers the complete ML workflow:
- Data Loading
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training

---

# 🎯 Objective
The goal of this project is to identify important factors affecting customer churn and build a predictive model to help businesses improve customer retention.

---

# 🚀 Project Workflow

## ✅ Day 1: Data Loading
- Loaded dataset using Pandas
- Explored dataset structure using `.info()` and `.shape()`
- Viewed sample data using `.head()`

---

## ✅ Day 2: Data Cleaning
- Converted `TotalCharges` from string to numeric
- Handled missing values
- Cleaned inconsistent data
- Prepared dataset for analysis

---

## ✅ Day 3: Exploratory Data Analysis (EDA)
- Visualized churn distribution
- Analyzed customer behavior using graphs
- Identified important churn patterns
- Observed higher churn in month-to-month contracts
- Observed higher churn among customers with shorter tenure

---

## ✅ Day 4: Feature Engineering and Model Training
- Removed unnecessary columns
- Converted categorical features into numeric format
- Applied one-hot encoding
- Split dataset into training and testing sets
- Trained Logistic Regression model
- Evaluated model accuracy

---

# 📈 Key Insights
- Customers with month-to-month contracts are more likely to churn
- Customers with higher monthly charges tend to churn more
- Customers with shorter tenure have higher churn rates
- Long-term customers are more likely to stay

---

# 🤖 Machine Learning

## ✅ Model Used
- Logistic Regression

## ✅ Evaluation Metric
- Accuracy Score

## ✅ Model Accuracy
- Achieved approximately **82% accuracy**

---

# 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# 📊 Dataset
The project uses the **Telco Customer Churn Dataset**, which contains:
- Customer demographics
- Services subscribed
- Billing information
- Customer churn status

---

# 📂 Project Structure

```text
churn-prediction-ml/
│
├── data/
│   └── churn.csv
│
├── notebooks/
│   ├── day1_data_loading.py
│   ├── day2_data_cleaning.py
│   ├── day3_eda.py
│   └── day4_feature_engineering_and_model_training.py
│
├── README.md
└── requirements.txt
```

---

# ⭐ Conclusion
This project demonstrates a complete Machine Learning workflow for customer churn prediction, including preprocessing, visualization, feature engineering, and predictive modeling.
