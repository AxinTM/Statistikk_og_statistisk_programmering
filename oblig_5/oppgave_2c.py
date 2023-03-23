import numpy as np
import scipy.stats as stats

p_verdi = stats.t.sf(3.535, 9)
print(f"p-verdien er: {p_verdi}")
