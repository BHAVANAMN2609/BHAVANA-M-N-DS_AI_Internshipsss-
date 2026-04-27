import pandas as pd
df = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK ", 
                 "Los Angeles", " los angeles ", "LOS ANGELES"]
})
print("Unique values BEFORE cleaning:\n")
print(df["Location"].unique())
df["Location"] = (
    df["Location"]
    .str.strip()      
    .str.title()      
)
print("\nUnique values AFTER cleaning:\n")
print(df["Location"].unique())