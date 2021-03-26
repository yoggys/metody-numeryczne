import numpy as np

def jacobi(a, vx, vb, n):
    alfa = -np.array(a)
    np.fill_diagonal(alfa, 0)
    alfa = (alfa.T/np.diag(a)).T
    beta = vb/np.diag(a)
    for _ in range(n):
        vx = beta+np.dot(alfa, vx)

    return list(vx)
        
if __name__ == "__main__":
    try:
        a = [[4,1,1], [3,5,1], [1,1,3]]
        b = [1,2,3]
        vx = [0,0,0]
        n = 10
        print(jacobi(a, vx, b, n))
        print(list(np.linalg.solve(a, b)))
    except Exception as E:
        print(E)
            
