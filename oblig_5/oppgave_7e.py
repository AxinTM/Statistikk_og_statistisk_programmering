import scipy.stats as stats
p_0 = 0.05
alpha = float(input("Oppgi signifikansnivå (alpha): "))
H_0 = f"De 74 flaskene er et tilfeldig utvalg"
H_1 = f"De 74 flaskene er ikke et tilfeldig utvalg"
Z = 3.894
k = 11
n = 74


p_test = stats.binomtest(k, n, p_0, alternative="greater")

print(f"p-verdien er: {p_test.pvalue}")

if p_test.pvalue <= alpha:
    print(f"{H_1}, vi forkaster H_0 på signifikantnivå {alpha}")
else:
    print(f"{H_0}, vi forkaster ikke H_0 på signifikantnivå {alpha}")
