import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.interpolate import CubicSpline

import warnings
warnings.simplefilter("ignore")

"""
Otrzymywany w programie (rozwinięty o dodatkowe rzeczy) wykres jest animowany i kolejno przedstawia:
- punkty z wylosowanymi wartościami losowo z zakresu -5,5
- dopasowane funkcje sklejone
- każdą z funkcji sklejonych oddzielnie

xlsk, xpsk, points - to kolejno lewa, prawa granica punktów oraz ich ilość
"""

#zwracana losowa funkcja
def func():
    """Zwracana losowa wartość w podanym przedziale."""
    return random.randrange(-5,5)

def calc(x, a, b, c, d):
    """Obliczana wartość dla zdefiniowanej poniżej funkcji."""
    return a*x**3+b*x**2+c*x+d

if __name__ == "__main__":
    xlsk, xpsk, points = -5, 5, random.randint(3,6)
    x = np.linspace(xlsk, xpsk, points)
    y = [func() for _ in x]

    cs = CubicSpline(x, y, bc_type="natural")

    #maksymalizacja okna dla systemu windows oraz zmiana tytułu okna // zakomentować window.state jeśli są problemy
    mng = plt.get_current_fig_manager()
    mng.set_window_title("Animacja dla interpolacji zbioru punktów funkcjami sklejanymi")
    mng.window.state('zoomed')

    #zgrupowane wyniki
    plt.title(f"Interpolacja zbioru punktów funkcjami sklejanymi")
    plt.plot(x, y, 'ro', label="Punkty funkcji początkowej")
    plt.ylim(max(y)+1,min(x)-1)
    plt.legend()
    plt.pause(0.5)

    xfit = np.linspace(xlsk-4,xpsk+4,100)
    yfit = cs(xfit)
    plt.plot(xfit, yfit, label="Dopasowanie sklejonych funkcji")
    plt.legend()

    for it in range(cs.c.shape[1]):
        coefficients = [cs.c[x][it] for x in range(cs.c.shape[0])]
        print(coefficients)
        plt.pause(0.5)
        xi = np.linspace(xlsk-3, xpsk+3, 100)
        plt.plot(xi, calc(xi-x[it], *coefficients), label=f"Sklejona funkcja nr. {it+1} dla ({x[it]:.2f};{x[it+1]:.2f})")
        plt.legend()

    plt.show()
    plt.close()
