import numpy as np
import time
import scipy.integrate as integrate

def func(x):
    return np.sin(x)

def trapez(f, a, b, h):
    x = np.arange(a, b+h, h)
    s = np.sum(f(x) - 0.5*f(a) - 0.5*f(b))
    return h*s

a = 0
b = np.pi
h = (b-a)/100000000

#trap
time_s = time.perf_counter()
c = trapez(func, a, b, h)
time_e = time.perf_counter()
print(f"wynik: {c} \nczas: {time_e-time_s}")

#scipy
time_s = time.perf_counter()
c = integrate.quad(func, a, b)[0]
time_e = time.perf_counter()
print(f"wynik: {c} \nczas: {time_e-time_s}")


#dbl integrate //circle
def f(x, y):
    return 1
def g(x):
    return np.sqrt(1-x**2)

c = 4*integrate.dblquad(f,0,1,0,g)[0]
print(c)