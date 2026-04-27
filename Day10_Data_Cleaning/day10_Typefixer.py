import pandas as pd
data = {
    "ProductID": [1, 2, 3, 4],
    "ProductName": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": ["$750.00", "$25.50", "$45.99", "$199.99"],  
    "Date": ["2026-01-01", "2026-01-03", "2026-01-05", "2026-01-07"]  
}
df = pd.DataFrame(data)
print("Before Conversion:\n")
print(df.dtypes)
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])
print("\nAfter Conversion:\n")
print(df.dtypes)
print("\nUpdated DataFrame:\n")
print(df)