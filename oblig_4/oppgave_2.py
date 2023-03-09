import numpy as np
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt

# Les inn data fra fil
data = np.genfromtxt("katters_vekt.csv", delimiter=",", skip_header=1)

# Velg kolonnene som inneholder vektdataene
kattevekt = data[:, 2]
hjertevekt = data[:, 3] / 1000  # Konverter hjertevekt fra gram til kg

# Lag QQ-plott for kattens vekt

vektKatt = qqplot(kattevekt, line='s')
vektKatt.suptitle("QQ-plot for kattens vekt")
plt.show()

# Lag QQ-plott for hjertenes vekt

hjerteVekt = qqplot(hjertevekt, line='s')
hjerteVekt.suptitle("QQ-plot for hjertenes vekt")
plt.show()