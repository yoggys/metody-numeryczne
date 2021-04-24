import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def func(x, a, b, c, d):
    return a*np.sin(x*b)+c*np.exp(-d*x**2)

xlsk, xpsk, points = -5, 5, 100
amp = 10
x = np.linspace(xlsk, xpsk, points)
y = func(x, 1, 2, 3, 4) + amp*np.random.normal(size=len(x))

params, covariance = opt.curve_fit(func, x, y)

plt.plot(x, y, 'ro')
plt.plot(x, func(x, *params))
plt.plot(x, func(x, 1,2,3,4))
plt.show()
