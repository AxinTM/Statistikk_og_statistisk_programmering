import numpy as np
import scipy.stats as stats

# Les inn data fra fil
data = np.genfromtxt("katters_vekt.csv", delimiter=",", skip_header=1)

# Velg kolonnene som inneholder vektdataene
kattevekt = data[:, 2]
hjertevekt = data[:, 3]

r = stats.pearsonr(kattevekt, hjertevekt)

print(f"Korrelasjonskoeffisienten mellom datasettene er: {r[0]}")