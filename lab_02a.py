def f(x):
    return x**2-x-1

def bisection(func, left, right, p):
    while True:
        mid = (left+right)/2
        if right-left < p:
            return [mid, right-left]
        if func(left)*func(mid) < 0:
            right = mid
        elif func(right)*func(mid) < 0:
            left = mid
        elif func(mid) == 0:
            return [mid, 0]
        else:
            return None

if __name__ == "__main__":
    while True:
        try:
            try:
                a = float(input("Podaj lewy brzeg badanego przedziału: "))
                b = float(input("Podaj prawy brzeg badanego przedziału: "))
                n = float(input("Podaj wymaganą maksymalną precyzje obliczeń (>0): "))
            except:
                raise ValueError("[ERROR] podano błędne dane!")
            if n<=0 or a==b:
                raise ValueError("[ERROR] precyzja powinna być >0, a lewy brzeg różny od prawego!")

            if a>b:
                tmp = a
                a = b
                b = tmp
                del tmp

            out = bisection(f, a, b, n)

            if out is None:
                print("Brak miejsca zerowego w badanym przedziale!")
            else:
                print(f"Miejsce zerowe: {out[0]} \nOtrzymana precyzja: {out[1]}") 
                
            break
        except ValueError as E:
            print(E)

