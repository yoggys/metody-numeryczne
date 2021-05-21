import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation

import warnings
warnings.simplefilter("ignore")

def func1(wp, t):
    du = np.zeros(4)
    du[0] = wp[1]
    du[1] = (-3*np.sin(wp[0]) - np.sin(wp[0]-2*wp[2]) - 2*np.sin(wp[0]-wp[2])*((wp[3]**2)+(wp[1]**2)*np.cos(wp[0]-wp[2])))/(3-np.cos(2*wp[0]-wp[2]))
    du[2] = wp[3]
    du[3] = (2*np.sin(wp[0]-wp[2])*(2*(wp[1]**2)+2*np.cos(wp[0])+(wp[3]**2)*np.cos(wp[0]-wp[2])))/(3-np.cos(2*wp[0]-wp[2]))
    return du


if __name__ == "__main__":
    wp = [np.pi/2,0, np.pi/2, 0]
    tmax = 1000
    n = 2000

    t = np.linspace(0, tmax, n)
    out = odeint(func1, wp, t)
    theta1 = out[:, 0]
    x1 = np.sin(theta1)
    y1 = -np.cos(theta1)

    theta2 = out[:, 2]
    x2 = x1 + np.sin(theta2)
    y2 = y1 + -np.cos(theta2)

    def update(i):
        plt.clf()
        plt.axis([-2,2, -2,2])

        plt.plot([0,x1[i]], [0,y1[i]])
        plt.plot([x1[i]], [y1[i]], 'o')

        plt.plot([x1[i], x2[i]], [y1[i], y2[i]])
        plt.plot([x2[i]], [y2[i]], 'o')
        plt.axis('off')

    fig = plt.figure("Podójne wahadło")
    anim = animation.FuncAnimation(fig, update, frames=n, interval=1)
    
    #we wzorach z PD nie są uwzględnione siły tarcia więc wahadła mogą zacząć w pewnym momencie wariować
    plt.show()
