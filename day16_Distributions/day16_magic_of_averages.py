import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

population = np.random.exponential(scale=50000, size=100000)

plt.hist(population, bins=50)
plt.title("Original Skewed Population (Income)")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)
plt.hist(sample_means, bins=30)
plt.title("Distribution of Sample Means (n = 30)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
