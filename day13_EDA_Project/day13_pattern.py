import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")

# ----------------------------------
# 1️⃣ Correlation Matrix
# ----------------------------------
corr = df.corr(numeric_only=True)
print("Correlation Matrix:\n", corr)

plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# ----------------------------------
# 2️⃣ Identify Highly Correlated Features (> 0.8)
# ----------------------------------
print("\nHighly Correlated Pairs (>|0.8|):")

for i in corr.columns:
    for j in corr.columns:
        if i != j and abs(corr.loc[i, j]) > 0.8:
            print(f"{i} and {j} -> {corr.loc[i, j]}")

# ----------------------------------
# 3️⃣ Boxplot for Outliers (Price)
# ----------------------------------
plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price (Outlier Detection)")
plt.show()

print("\nObservation: Boxplot helps identify extreme values (outliers) in Price.")