import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")   

print("Skewness:", df["Price"].skew())
print("Kurtosis:", df["Price"].kurt())

plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.show()

plt.figure()
sns.countplot(x=df["City"])
plt.title("City Count Plot")
plt.xticks(rotation=45)
plt.show()

print("Most Frequent City:", df["City"].value_counts().idxmax()) 