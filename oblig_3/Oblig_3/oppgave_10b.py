import scipy.stats as stats

#Oppgave 10b
N = 760
σ = 10
x = float(input(f"Hvor mye tror du brødet veier? \n"
                f"Tast inn vekten du tror:  "))

normalfordeling = stats.norm.cdf(x, N, σ)

print(f"\nSannsynligheten for at brødet veier mer enn det du tror er: {1-normalfordeling}")