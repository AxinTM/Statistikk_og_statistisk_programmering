import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

#Oppgave 10a
N = 760
σ = 10
x = np.arange(720, 800)

normalfordeling = stats.norm.pdf(x, N, σ)

plt.title("Normalfordeling")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, normalfordeling)
plt.show()
