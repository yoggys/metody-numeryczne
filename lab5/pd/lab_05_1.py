import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def func(x, a, b, c, d):
    return a*np.sin(x*b)+c*np.exp(-d*x**2)

if __name__ == "__main__":
    xlsk, xpsk, points = -5, 5, 10
    amp = 0.1
    x = np.linspace(xlsk, xpsk, points)
    y = func(x, 1, 2, 3, 4) + amp*np.random.normal(size=len(x))

    params, covariance = opt.curve_fit(func, x, y)

    plt.plot(x, y, 'ro', label="Zaszumione wartości funkcji")
    xi = np.linspace(xlsk, xpsk, points*10)
    plt.plot(xi, func(xi, 1,2,3,4), label="Bezpośrednio policzone wartości funkcji")
    plt.plot(xi, func(xi, *params), label="Dopasowana funkcja (curve_fit)")
    plt.legend()

    #maksymalizacja okna dla systemu windows // zakomentować window.state jeśli są problemy
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    plt.show()
