import scipy.stats as stats

print("Oppgave 3a")
N = 64
n = 8
M = 14

print(f"Sannsynligheten for (X=3): {stats.hypergeom.pmf(3, N, M, n)}")
print(f"Sannsynligheten for (X<=3): {stats.hypergeom.cdf(3, N, M, n)}\n")

print("Oppgave 3b")

print(f"Sannsynligheten for (X=3): {stats.binom.pmf(3, n, 14/64)}")
print(f"Sannsynligheten for (X<=3): {stats.binom.cdf(3, n, 14/64)}\n")

print("Oppgave 3c")
N = 640
n = 8
M = 140

print(f"Sannsynligheten for (Y=3): {stats.hypergeom.pmf(3, N, M, n)}")
print(f"Sannsynligheten for (Y<=3): {stats.hypergeom.cdf(3, N, M, n)}\n")

print("Oppgave 3d")
print(f"Sannsynligheten for (X=3): {stats.binom.pmf(3, n, 14/64)}")
print(f"Sannsynligheten for (X<=3): {stats.binom.cdf(3, n, 14/64)}")

