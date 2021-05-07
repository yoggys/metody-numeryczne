import networkx as nx
import matplotlib.colors as col
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

if __name__ == "__main__":
    size = random.randint(10,100)
    A = nx.gnm_random_graph(size, size*5, directed=True)

    alfa = random.random()
    vals = []
    tmp = 1.1
    while True:
        tmp = tmp-0.1
        if tmp > 0:
            val, vect = power2(A, tmp)
            vals.append(val)
        else:
            break
    del tmp

    #zmiana wartości alfa na mniejszą wpływa na zmniejszenie wartości części rzeczywistej oraz urojonej
    #druga największa wartość własna w metodzie potęgowej określa zbiezność (poprzez iloraz λ1 oraz λ2)
    #czym λ2 jest bardziej zbliżone  do λ1 tym wolniejsza zbieżność

    fig, ax = plt.subplots()
    ax.set_title("Powstały graf dla wygenerowanych macierzy Google")

    #maksymalizacja okna dla systemu windows oraz zmiana tytułu okna
    mng = plt.get_current_fig_manager()
    mng.set_window_title('Powstały graf dla wygenerowanych macierzy Google')
    mng.window.state('zoomed')

    t = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(t), np.sin(t), 'k')

    data = {}
    for i in range(len(vals)):
        data[f'x{i}'] = vals[i].real
        data[f'y{i}'] = vals[i].imag

    df = pd.DataFrame(data)

    colors = list(col.XKCD_COLORS.values())
    for i in range(len(vals)):
        df.plot(x=f"x{i}", y=f"y{i}", s=10, color=colors[random.randint(0, len(colors)-1)], kind='scatter', ax=ax, label=f"G matrix α={1-i*0.1}")
        ax.legend(loc='upper right')
        ax.set_xlabel("Real vals")
        ax.set_ylabel("Imag vals")
        ax.axis('equal')
        plt.pause(0.3)


    plt.show()
    plt.clf()
    plt.close()
