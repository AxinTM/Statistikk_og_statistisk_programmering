import math
import scipy.stats

# Les inn data fra fil
filename = input("Skriv inn navnet på filen med målingene: ")
data = np.loadtxt(filename, delimiter=',')

