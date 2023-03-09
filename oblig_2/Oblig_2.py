import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

n = int(input("Number of try: "))
p = float(input("Probability for each try: "))
k = np.arange(n+1)

print("\n")
print(f"Point probability: {(stats.binom.pmf(k, n, p))}\n")

print(f"Cumulative probability: {(stats.binom.cdf(k, n, p))}\n")


plt.bar(k, stats.binom.pmf(k, n, p))
plt.show()
plt.step(k, stats.binom.cdf(k, n, p), where="post")
plt.show()
