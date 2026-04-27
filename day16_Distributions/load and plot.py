import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

plt.figure()
sns.histplot(df["Score"], kde=True)

plt.title("Histogram with KDE Overlay")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.show()
