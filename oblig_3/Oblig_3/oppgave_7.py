import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

λt = (float(input("Tast inn ønsket λt: ")))
x = float(input(f"Tast inn ønsket øvre grense: "))
range1 = np.arange(0, x+1, 1)
poissf =stats.poisson.pmf(range1, λt)
plt.plot(range1, poissf, linestyle="dashdot")
poissf =stats.poisson.pmf(range1, λt+30)
plt.plot(range1, poissf, linestyle="dashdot")
poissf =stats.poisson.pmf(range1, λt+60)
plt.plot(range1, poissf,linestyle="dashdot")


plt.show()

