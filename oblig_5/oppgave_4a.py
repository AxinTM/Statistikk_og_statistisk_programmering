import numpy as np
import scipy.stats as stats

# Les inn dataene fra CSV-filen
data = np.genfromtxt("katters_vekt.csv", delimiter=",", skip_header=1)

# Velg kolonnene som inneholder vektdataene
kattevekt = data[:, 2]

# Angi hypotesene
my_0 = float(input("Oppgi forventeningsverdien (my_0): "))
alpha = float(input("Oppgi signifikansnivå (alpha): "))
# oppgave a:
H_0 = f"Gjennomsnittsvekten er lik eller mindre enn {my_0} kg"
H_1 = f"Gjennomsnittsvekten er større enn {my_0} kg"

# oppgave b, utfør hypotesetesten
t, p = stats.ttest_1samp(kattevekt, my_0, alternative="greater")
df = len(kattevekt) - 1
kritisk_verdi = stats.t.ppf(1 - alpha, df)

# Skriv ut resultatene
print(f"Hypotese: {H_0}")
print(f"Hypotese: {H_1}")
print(f"Testobservator (t): {t:.5f}")
print(f"Kritisk verdi: {kritisk_verdi:.5f}")
#oppgave c, d, e:
if t > kritisk_verdi:
    print(f"Resultat: Forkast H_0 til fordel for H_1 på signifikatnivå {alpha}, (p-verdi: {p:.5f})")
else:
    print(f"Resultat: Behold H_0 på signifikantnivå {alpha}, (p-verdi: {p:.5f})")