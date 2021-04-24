import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import math

def func(x, a, b, c, d):
    return a*math.sin(x*b)+c*math.exp(-d*x**2)

xlsk, xpsk, points = -5, 5, 20
amp = 1
f = np.vectorize(func)
x = np.linspace(xlsk, xpsk, points)
y = (f(x, 1, 2, 3, 4)) + amp*np.random.normal(size=len(x))

plt.plot(x, y, 'ro')
plt.plot(x, f(x, 1,2,3,4))
plt.show()
