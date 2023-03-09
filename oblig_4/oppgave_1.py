import scipy.stats as stats
import random
import math
import matplotlib.pyplot as plt
import numpy as np

#Oppgave 1b
terningKast = int(input(f"Tast inn antall kast du ønsker: "))
omganger = int(input(f"Tast inn antall omganger du ønsker å spille: "))

i = 0
σ = 1.71
resultatAvOmganger = []

while i < omganger:
    sumAvTerning = 0
    for x in range(terningKast):
        sumAvTerning += random.randint(1, 6)

        gjennomsnitt = sumAvTerning/terningKast
    print(f"Omgang: {[i+1]}\n"
            f"Antall kast: {terningKast}\n"
            f"Sum av øyer: {sumAvTerning}\n"
            f"Gjennomsnitt av alle kast: {gjennomsnitt} ")
    i += 1

    resultatAvOmganger.append(gjennomsnitt)
plt.xlabel('Forventningsverdi til terningkast')
plt.ylabel('y')
plt.hist(resultatAvOmganger, bins=30, edgecolor="black")
plt.show()
print("\n")
#Oppgave 1c

gjennomsnittAvGjennomsnitt = np.mean(resultatAvOmganger)
stdAvGjennomsnitt = np.std(resultatAvOmganger, ddof=1)

print(f"Gjennomsnittet av alle gjennomsnittene: {gjennomsnittAvGjennomsnitt:.3f}")
print(f"Standardavviket av alle gjennomsnittene: {stdAvGjennomsnitt:.3f}")
