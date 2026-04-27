# ==========================================================
# MINI PROJECT 1 – EXPLORATORY DATA ANALYSIS (EDA)
# Dataset: Customer Analytics
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# ==============================
# PHASE 1 – DATASET INSPECTION
# ==============================

print("\n==============================")
print("PHASE 1 – DATASET INSPECTION")
print("==============================")

df = pd.read_csv("customer_analytics.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())


# ==============================
# PHASE 2 – DATA CLEANING
# ==============================

print("\n==============================")
print("PHASE 2 – DATA CLEANING")
print("==============================")

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill numeric columns with median
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ==============================
# PHASE 3 – CLEAN VISUAL DASHBOARD
# ==============================

print("\n==============================")
print("VISUAL DASHBOARD")
print("==============================")

fig = plt.figure(figsize=(22,12))
plt.subplots_adjust(hspace=0.35, wspace=0.30)

# Select first two numeric columns for visualization
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

# 1️⃣ Distribution of first numeric column
if len(num_cols) > 0:
    ax1 = plt.subplot(2,3,1)
    sns.histplot(df[num_cols[0]], kde=True)
    ax1.set_title(f"{num_cols[0]} Distribution")

# 2️⃣ Distribution of second numeric column
if len(num_cols) > 1:
    ax2 = plt.subplot(2,3,2)
    sns.histplot(df[num_cols[1]], kde=True)
    ax2.set_title(f"{num_cols[1]} Distribution")

# 3️⃣ Count plot of first categorical column
cat_cols = df.select_dtypes(include=['object']).columns
if len(cat_cols) > 0:
    ax3 = plt.subplot(2,3,3)
    sns.countplot(x=cat_cols[0], data=df)
    ax3.set_title(f"{cat_cols[0]} Distribution")
    plt.xticks(rotation=30)

# 4️⃣ Boxplot between first categorical & first numeric
if len(cat_cols) > 0 and len(num_cols) > 0:
    ax4 = plt.subplot(2,3,4)
    sns.boxplot(x=cat_cols[0], y=num_cols[0], data=df)
    ax4.set_title(f"{num_cols[0]} vs {cat_cols[0]}")
    plt.xticks(rotation=30)

# 5️⃣ Scatter plot between first two numeric columns
if len(num_cols) > 1:
    ax5 = plt.subplot(2,3,5)
    sns.scatterplot(x=num_cols[0], y=num_cols[1], data=df)
    ax5.set_title(f"{num_cols[0]} vs {num_cols[1]}")

# 6️⃣ Correlation Heatmap
ax6 = plt.subplot(2,3,6)
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, fmt=".2f", cmap="coolwarm")
ax6.set_title("Correlation Matrix")

plt.suptitle(
    "Customer Analytics – Exploratory Data Analysis Dashboard",
    fontsize=16,
    fontweight="bold"
)

plt.show()


# ==============================
# EXECUTIVE SUMMARY
# ==============================

print("\n==============================")
print("EXECUTIVE SUMMARY")
print("==============================")

print("""
1. Numeric variables show distribution patterns useful for customer segmentation.
2. Categorical variables reveal group differences.
3. Correlation analysis helps identify relationships between customer features.
4. Data cleaning ensured no missing or duplicate records.
5. EDA provides insights for business decision-making.
""")

print("EDA Project Completed Successfully.")