import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation

import warnings
warnings.simplefilter("ignore")

def func(wp, t):
    du = np.zeros(2)
    du[0] = wp[1]
    du[1] = -gamma*wp[1] - np.sin(wp[0])
    return du

if __name__ == "__main__":
    #warunki początkowe
    wp = [np.pi/2, 0]
    wp2 = [np.pi/2, 0]
    gamma = 0.1 
    tmax = 1000
    n = 2000

    t = np.linspace(0, tmax, n)
    out = odeint(func, wp, t)
    theta1 = out[:, 0]
    x1 = np.sin(theta1)
    y1 = -np.cos(theta1)
    
    def update(i):
        plt.clf()
        plt.axis([-4,4, -4,4])

        plt.plot([0,x1[i]], [0,y1[i]])
        plt.plot([x1[i]], [y1[i]], 'o')
        plt.axis('off')

    fig = plt.figure("Wahadło")
    anim = animation.FuncAnimation(fig, update, frames=n, interval=20)
    plt.show()
