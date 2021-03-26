import numpy as np

def check(a, vx):
    lgth = len(vx)
    for i in range(lgth):
        #a[i][i] < sum(a[i]...)-a[i][i]
        if 2*a[i][i] < sum([a[i][j] for j in range(lgth)]):
            raise Exception("Nie jest przekątniowo dominująca!")

def jacobi(a, vx, vb, n):
    check(a, vx)
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
            
