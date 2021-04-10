import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.unweighted import predecessor
import numpy as np

def power(A, N):
    B = nx.stochastic_graph(A)
    H = nx.to_numpy_array(B).T
    n = H.shape[0]
    x = np.zeros(n)
    x[0] = 1
    for i in range(N):
        x = np.dot(H, x)

    return x

def power2(A):
    B = nx.stochastic_graph(A)
    H = nx.to_numpy_array(B).T
    val, vect = np.linalg.eig(H)
    return val, vect
    

edgelist = [(1,2), (1,3), (2,4), (4,2), (3,2), (3,5), (4,5), (4,6), (5,6), (5,7), (5,8), (6,8), (7,1), (7,5), (7,8), (8,6)]
A = nx.DiGraph(edgelist)

#nx.draw(A, with_labels=True)
#plt.show()

np.set_printoptions(precision=2, suppress=True)
print(power(A, 30))
val, vect = power2(A)
plt.scatter(val.real, val.imag)
t = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(t), np.sin(t), 'k')
plt.axis('equal')
plt.show()

