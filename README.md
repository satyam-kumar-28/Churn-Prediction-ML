# Customer Churn Analysis Project

## 📌 Overview
This project analyzes customer churn data and identifies key factors influencing customer retention using Python, Pandas, and visualization techniques.

## 🚀 Day 1: Data Loading
- Loaded dataset using Pandas
- Checked structure using `.info()`, `.shape()`
- Viewed sample data using `.head()`

## 🚀 Day 2: Data Cleaning
- Converted `TotalCharges` from string to numeric
- Handled missing values
- Converted categorical data (Yes/No → 1/0)

## 🚀 Day 3: Exploratory Data Analysis (EDA)
- Visualized churn distribution
- Identified patterns between customer features and churn
- Observed higher churn in month-to-month contracts
- Customers with shorter tenure are more likely to churn

## 📂 Project Structure

```
churn-prediction-ml/
│
├── data/
│   └── churn.csv
│
├── notebooks/
│   ├── day1_data_loading.py
│   ├── day2_data_cleaning.py
│   └── day3_eda.py
│
├── README.md
└── requirements.txt
```

## 🛠️ Tech Used
- Python
- Pandas
- Matplotlib
- Seaborn

## 📊 Dataset
Telco Customer Churn dataset containing customer demographics, services, and billing information.

## 🔜 Next Steps
- Feature Engineering
- Machine Learning Model
- Prediction System