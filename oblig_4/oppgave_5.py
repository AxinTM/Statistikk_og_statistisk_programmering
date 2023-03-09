import math
from scipy import stats


# Funksjon for å beregne konfidensintervall
def binom_ci(n, p, alpha):
    # Sjekk om tilnærmingen er gyldig
    if n * p * (1 - p) >= 5:
        z = abs(stats.norm.ppf((1 - alpha) / 2))
        se = z * math.sqrt(p * (1 - p) / n)
        lower = p - se
        upper = p + se
        print(f"[{round(lower, 6)}, {round(upper, 6)}]")
    else:
        print("Tilnærmingen er ikke gyldig. Prøv med større utvalgsstørrelse eller endre andelen.")
        return None


# Les inn brukerinput
n = int(input("Skriv inn utvalgets størrelse: "))
x = float(input("Skriv inn andelen i utvalget som er i favør av det du sjekker: "))
p_hat = x / n
alpha = float(input("Skriv inn konfidensintervallet i prosent: ")) / 100

# Skriv ut konfidensintervallet
binom_ci(n, p_hat, alpha)

