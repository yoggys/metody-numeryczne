import time

def f(x):
    return x**2-x-1

def bisection(f, a, b, N):
    left = a
    right = b

    for _ in range(N):
        mid = (left+right)/2
        if f(left)*f(mid) < 0:
            right = mid
        elif f(right)*f(mid) < 0:
            left = mid
        elif f(mid) == 0:
            return mid
        else:
            return None
    return mid

if __name__ == "__main__":
    while True:
        try:
            try:
                a = float(input("Podaj lewy brzeg badanego przedziału: "))
                b = float(input("Podaj prawy brzeg badanego przedziału: "))
                n = int(input("Podaj liczbę iteracji: "))
            except:
                raise ValueError("[ERROR] podano błędne dane!")
            if n<=0 or a==b:
                raise ValueError("[ERROR] precyzja powinna być >0, a lewy brzeg różny od prawego!!")

            if a>b:
                tmp = a
                a = b
                b = tmp
                del tmp

            begin = time.time()
            out = bisection(f, a, b, n)
            end = time.time()

            if out is None:
                print("Brak miejsca zerowego w badanym przedziale!")
            else:
                print(f"Miejsce zerowe: {out}")
                print(f"Trwało to: {(end-begin):.20f} sekund")
                
            break
        except ValueError as E:
            print(E)