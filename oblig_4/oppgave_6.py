import math
import numpy as np
from scipy import stats

# Leser inn data fra fil
filename = input("Skriv inn navnet på filen med målingene: ")
data = np.loadtxt(filename, delimiter=',')

# Beregner punktestimat for standardavviket
n = len(data)
s2 = np.var(data, ddof=1)
s_estimator = np.std(data, ddof = 1)
print(f"Punktestimat for standardavvik:, {round(s_estimator,1)}")

# Beregner konfidensintervaller
alpha = float(input("Skriv inn ønsket konfidensnivå i prosent (f.eks. 90 eller 95): ")) / 100
dof = n - 1  # frihetsgrader
alpha_2 = (1 - alpha) / 2

chi1 = stats.chi2.ppf(1 - alpha_2, dof)
nedre_grense = math.sqrt((dof * s2) / chi1)

chi2 = stats.chi2.ppf(alpha_2, dof)
øvre_grense = math.sqrt((dof * s2) / chi2)


print(f"konfidensintervall: [{nedre_grense}, {øvre_grense}]")