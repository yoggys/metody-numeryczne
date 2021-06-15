import numpy as np
import matplotlib.pyplot as plt

steps = 100
N = 1000
T = 2000
M = N  
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

for t in range(steps):
    spins, M = step(spins, M, T)
    m[t] = M/N

plt.figure()
plt.axis([0,steps, -1.1, 1.1])
plt.plot(range(steps), m)
plt.show()