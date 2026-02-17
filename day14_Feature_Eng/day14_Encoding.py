import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
}

df = pd.DataFrame(data)

# -----------------------------
# 1️⃣ Label Encoding (Binary Column)
# -----------------------------
le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

# -----------------------------
# 2️⃣ One-Hot Encoding (Nominal Column)
# -----------------------------
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print(df)
