import numpy as np

def check(a, vx):
    lgth = len(vx)
    for i in range(lgth):
        #a[i][i] < sum(a[i]...)-a[i][i]
        if 2*a[i][i] < sum([a[i][j] for j in range(lgth)]):
            raise Exception("Nie jest przekątniowo dominująca!")

def jacobi(a, vx, vb, n):
    check(a, vx)
    lgth = len(vx)
    vx_cp = vx.copy()
    for _ in range(n):
        for i in range(lgth):
            tmp = vb[i]
            for j in range(lgth):
                if(j!=i):
                    tmp -= a[i][j]*vx[j]
            vx_cp[i] = tmp/a[i][i]
        vx = vx_cp.copy()
    return vx
        
if __name__ == "__main__":
    try:
        a = [[4,1,1],[3,5,1],[1,1,3]]
        b = [1,2,3]
        vx = [0,0,0]
        print(jacobi(a, vx, b, 10))
        print(np.linalg.solve(a, b))
    except Exception as E:
        print(E)
            
