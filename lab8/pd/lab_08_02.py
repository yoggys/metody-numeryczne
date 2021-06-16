import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp

#w celu przyśpieszenia działania krok temperatury to 50 stopni
steps = 10
N = 1000
T = range(100, 2000, 50)
M = N  
MG = list()
MG_theo = list()
spins = np.ones(N)
m=np.zeros(steps)

def step(spins, M, T):
    for i in range(N):
        x = np.random.randint(N)
        sum = np.sum(spins) - spins[x]
        delthaE = 2 * spins[x] * sum
        if  delthaE <= 0 or np.random.rand() < np.exp(- delthaE / T):
            spins[x] *= -1
            M += 2 * spins[x]
    return spins, M

def func(m, T):
    return np.tanh((N-1)*m/T)-m

def theo(T):
    return sp.root_scalar(func, args=(T), method='secant', x0=1, x1=2).root

for TT in T:
    for t in range(steps):
        spins, M = step(spins, M, TT)
        m[t] = M/N
    MG.append(m[-1])
    MG_theo.append(theo(TT))

plt.figure("Wykres zależności magnetyzacji od temperatury")
plt.axis([0, T[-1], -1.1, 1.1])
plt.plot(T, MG, label="Krzywa przewidywana (doświadczalna)")
plt.plot(T, MG_theo, label="Krzywa teoretyczna")
plt.legend()
plt.show()