import pandas as pd
df=pd.read_csv(r"C:\Users\KIIT\Churn-Prediction-ML\data\Churn(1).csv")
df.head()
df.shape
df.info()
df.isnull().sum()
df.describe()
