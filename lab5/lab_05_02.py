import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.interpolate import CubicSpline

import warnings
warnings.simplefilter("ignore")

def func(x, a, b, c, d):
    return a*x**3+b*x**2+b*x+d

xlsk, xpsk, points = -5, 5, 100
amp = 10
x = np.linspace(xlsk, xpsk, points)
y = func(x, 1, 2, 3, 4)

params, covariance = opt.curve_fit(func, x, y)

cs = CubicSpline(x, y, bc_type="natural")


plt.plot(x, y, 'ro')
#plt.plot(x1, y2)
plt.show()
