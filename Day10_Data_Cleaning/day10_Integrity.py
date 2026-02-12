import pandas as pd
df = pd.read_csv("customer_orders.csv")
print("Shape before cleaning:", df.shape)
print("\nMissing Values Report:")
print(df.isna().sum())
numeric_columns = df.select_dtypes(include=['number']).columns
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())
df = df.drop_duplicates()
print("\nShape after cleaning:", df.shape)