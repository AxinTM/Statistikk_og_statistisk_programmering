#Oppgave2
import numpy as np

height = np.genfromtxt('Oblig_1.txt', delimiter=",")

#a
median = np.median(height)
print(f"Median for høyden til barna er: {median}")

#b
average = np.average(height)
print(f"Middelverdi for høyden til barna er: {average}")

#c
variance = np.var(height, ddof=1)
print(f"Varians for høyden til barna er: {variance}")

#d
standard_deviance = np.std(height, ddof=1)
print(f"Standaravvik for høyden til barna er: {standard_deviance}")


