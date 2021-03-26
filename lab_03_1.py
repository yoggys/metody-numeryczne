import numpy as np
import random

#sprawdzenie czy przekątniowo dominująca
def check(a, vx):
    lgth = len(vx)
    for i in range(lgth):
        #a[i][i] < sum(a[i]...)-a[i][i]
        if 2*a[i][i] < sum([a[i][j] for j in range(lgth)]):
            raise Exception("Nie jest przekątniowo dominująca!")

def jacobi(a, vx, vb, n):
    lgth = len(vx)
    check(a, vx)
    alfa = -np.array(a)
    np.fill_diagonal(alfa, 0)
    alfa = (alfa.T/np.diag(a)).T
    beta = vb/np.diag(a)
    for _ in range(n):
        vx = beta+np.dot(alfa, vx)
    return list(vx)
        
def MPD(n):
    a = np.random.random((n, n))
    for i in range(n):
        a[i][i] = n+abs(random.random())
    return a

if __name__ == "__main__":
    try:
        a = MPD(3)
        b = [1,2,3]
        vx = [0,0,0]
        n = 10
        print(f"Metoda Jacobiego: {jacobi(a, vx, b, n)}")
        print(f"Wbudowana funkcja np.linalg: {list(np.linalg.solve(a, b))}")
    except Exception as E:
        print(E)
            
