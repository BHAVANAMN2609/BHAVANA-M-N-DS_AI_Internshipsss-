import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
population = np.random.exponential(scale=50000, size=100000)
plt.figure()
sns.histplot(population, bins=50, kde=True)
plt.title("Original Skewed Data (Income Distribution)")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()
sample_means = []
for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)
plt.figure()
sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of Sample Means (n = 30, 1000 samples)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()