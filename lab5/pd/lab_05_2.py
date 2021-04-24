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
(są one konfiguracyjne i można wpisywać dowolne wartości dzięki funkcji calc)
"""

#zwracana losowa funkcja
def func():
    return random.randrange(-5,5)

#funkcja zdenfiniowana do liczenia wartości wielomianów dowolnego stopnia bazując na ilości współczynników
def calc(x, *args):
    calculated = 0
    degree = len(args)
    for ii in range(degree):
        calculated += args[ii]*x**(degree-ii)
    return calculated

xlsk, xpsk, points = -5, 5, random.randint(2,10)
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

xfit = np.linspace(xlsk-2,xpsk+2,100)
yfit = cs(xfit)
plt.plot(xfit, yfit, label="Dopasowanie sklejonych funkcji")
plt.legend()

ii = 1
for coefficients in cs.c:
    print(coefficients)
    plt.pause(0.5)
    xi = np.linspace(xlsk, xpsk, 100)
    plt.plot(xi, calc(xi, *coefficients), label=f"Sklejona funkcja nr. {ii}")
    plt.legend()
    ii+=1
del ii

plt.show()
plt.close()
