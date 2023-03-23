import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#oppgave a:

data = np.genfromtxt("katters_vekt.csv", delimiter=",", skip_header=1)
kattevekt = data[:, 2]
hjertevekt = data[:, 3]

plt.scatter(kattevekt, hjertevekt)
plt.show()

#oppgave b:
line = stats.linregress(kattevekt, hjertevekt)
alpha = line.intercept
beta = line.slope

print(f"alpha = {alpha}\n"
      f"beta = {beta}")
print(f"y = {alpha} + {beta}x")

#oppgave d:

