from Investor import Investor
from scipy.stats import skewnorm
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
current=24
iv=20
percentage = 0.05
def objective(params):
    alpha, scale = params
    # Calculate the percentile value of the target value
    percentile_value = skewnorm.cdf(iv, alpha, loc=current, scale=scale)
    # We want this to be close to the target percentile
    return (percentile_value - percentage) ** 2

# Initial guesses for alpha and scale
initial_guess = [-5, 2]

# Perform the minimization
result = minimize(objective, initial_guess, bounds=[(None, None), (0.1, None)])

print(result.x)
#difference = iv - current

random_numbers = skewnorm.rvs(result.x[0], current,result.x[1] , size=10000)
n, bins = np.histogram(random_numbers, bins=200)
actual_peak_index = np.where(n == max(n))[0][0]
actual_peak = bins[actual_peak_index]
random_numbers+= current-actual_peak
print(n[actual_peak_index],actual_peak)
#plt.plot(n)
plt.hist(random_numbers,bins=200)
plt.show()
