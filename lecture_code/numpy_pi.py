# numpy_pi.py
import numpy as np

# Monte Carlo estimation of pi
def calc_pi_device(samples):  
    x = np.random.random(size=samples)
    y = np.random.random(size=samples)
    within_unit_circle = (x * x + y * y) < 1.0
    return 4.0 * sum(within_unit_circle) / samples
