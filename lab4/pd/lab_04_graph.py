import networkx as nx
import matplotlib.pyplot as plt
import random

size = random.randint(10,20)
A = nx.gnm_random_graph(size, size*10, directed=True)

mng = plt.get_current_fig_manager()
mng.set_window_title('Powstały graf dla wygenerowanych macierzy Google')
mng.window.state('zoomed')

nx.draw(A)

plt.show()
plt.clf()
plt.close()