import numpy as np
import matplotlib.pyplot as plt

#w celu przyśpieszenia działania krok temperatury to 50 stopni
steps = 10
N = 1000
T = range(100, 2000, 50)
M = N  
MG = list()
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

for TT in T:
    for t in range(steps):
        spins, M = step(spins, M, TT)
        m[t] = M/N
    MG.append(m[-1])

plt.figure("Wykres zależności magnetyzacji od temperatury")
plt.axis([0, T[-1], -1.1, 1.1])
plt.plot(T, MG)
plt.show()