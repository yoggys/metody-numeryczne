import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

def power2(A, alfa : float):
    B = nx.stochastic_graph(A)
    H = nx.to_numpy_array(B).T
    G = alfa*H+(1-alfa)*np.ones(H.shape)/H.shape[0]
    val, vect = np.linalg.eig(G)
    return val, vect

size = random.randint(10,100)
A = nx.gnm_random_graph(size, size*10, directed=True)

alfa = random.random()
val1, vect1 = power2(A, 1)
val2, vect2 = power2(A, alfa)

#zmiana wartości alfa na mniejszą wpływa na zmniejszenie wartości części rzeczywistej oraz urojonej
#druga największa wartość własna w metodzie potęgowej określa zbiezność (poprzez iloraz λ1 oraz λ2)
#czym λ2 jest bardziej zbliżone do λ1 tym wolniejsza zbieżność

fig, ax = plt.subplots()

#maksymalizacja okna dla systemu windows oraz zmiana tytułu okna
mng = plt.get_current_fig_manager()
mng.set_window_title('Powstały graf dla wygenerowanych macierzy Google')
mng.window.state('zoomed')

t = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(t), np.sin(t), 'k')
df = pd.DataFrame({'x1': val1.real, 'y1': val1.imag, 'x2': val2.real, 'y2': val2.imag})
df.plot(x="x1", y="y1", kind='scatter', color='#08F7FE', ax=ax, title="Powstały graf dla wygenerowanych macierzy Google", label=f"G matrix α=1")
df.plot(x="x2", y="y2", kind='scatter', color='#FE53BB', ax=ax, label=f"G matrix α={alfa}")

ax.set_xlabel("Real vals")
ax.set_ylabel("Imag vals")
ax.axis('equal')
ax.legend(loc='upper right')

plt.show()
plt.clf()
plt.close()
