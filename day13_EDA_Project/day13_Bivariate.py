import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")

plt.figure()
sns.scatterplot(x=df["Area_sqft"], y=df["Price"])
plt.title("Area vs Price")
plt.xlabel("Area (sqft)")
plt.ylabel("Price")
plt.show()

plt.figure()
sns.boxplot(x=df["City"], y=df["Price"])
plt.title("City vs Price")
plt.xticks(rotation=45)
plt.show()

correlation = df["Area_sqft"].corr(df["Price"])
print("Correlation between Area and Price:", correlation)

if correlation > 0:
    print("Observation: As Area increases, Price tends to increase.")
elif correlation < 0:
    print("Observation: As Area increases, Price tends to decrease.")
else:
    print("Observation: No clear relationship between Area and Price.")