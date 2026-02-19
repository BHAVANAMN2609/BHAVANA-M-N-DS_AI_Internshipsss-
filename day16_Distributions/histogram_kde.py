import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=1000)

df = pd.DataFrame({"Scores": data})

plt.figure()
sns.histplot(df["Scores"], kde=True)

plt.title("Histogram with KDE Overlay")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.show()