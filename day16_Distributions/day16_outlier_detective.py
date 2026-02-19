import pandas as pd

df = pd.read_csv("iris.csv") 
print(df.head()) 

column_name = "sepal_length"

mu = df[column_name].mean()
sigma = df[column_name].std()

df["z_score"] = (df[column_name] - mu) / sigma

outliers = df[abs(df["z_score"]) > 3]

print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)
print("Number of Outliers:", outliers.shape[0])
print(outliers)