import numpy as np
import time
import scipy.integrate as integrate

def func(x):
    return np.sin(x)

def trapez(f, a, b, h):
    x = np.arange(a, b+h, h)
    s = np.sum(f(x) - 0.5*f(a) - 0.5*f(b))
    return h*s

def romberg(f, a, b, n):
    def count_I(R1, R2, k):
        p4 = 4**k
        return (p4*R2-R1)/(p4-1)

    h = (b-a)
    current = list()
    latest = list()

    #inicjalizacja n-elementowej listy
    for ii in range(0, n):
        latest.append(trapez(f, a, b, h/2**(ii-1)))

    #obliczenie kolejno 2, 3, ..., n rzędu
    for i in range(1, n):
        for ii in range(0, n-i):
            current.append(count_I(latest[ii],  latest[ii+1], ii+1))

        #jeśli został 1 element zwracamy jego wartość, jeśli ilość elementów >1 przechodzimy do kolejnego rzędu
        if len(current) == 1:
            return current[0]
        else:
            latest = current.copy()
            current.clear()

if __name__ == "__main__":
    #definicja granic
    a = 0
    b = np.pi

    #trapez
    time_s = time.perf_counter()
    h = (b-a)/100000000
    result = trapez(func, a, b, h)
    time_e = time.perf_counter()
    print("\n// Metoda trapezów //")
    print(f"wynik: {result} \nczas: {time_e-time_s}\n")

    #scipy
    time_s = time.perf_counter()
    result = integrate.quad(func, a, b)[0]
    time_e = time.perf_counter()
    print("// Użycie scipy.quad //")
    print(f"wynik: {result} \nczas: {time_e-time_s}\n")

    #scipy romberg
    time_s = time.perf_counter()
    result = integrate.romberg(func, a, b)
    time_e = time.perf_counter()
    print("// Użycie scipy.romberg //")
    print(f"wynik: {result} \nczas: {time_e-time_s}\n")

    #romberg
    time_s = time.perf_counter()
    n = 21
    result = romberg(func, a, b, n)
    time_e = time.perf_counter()
    print(f"// Metoda Romberg'a (n={n}) //")
    print(f"wynik: {result} \nczas: {time_e-time_s}\n")