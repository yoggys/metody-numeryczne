def zad1(max):
    for i in range(1, max+1):
        print(f"x={i}, x^2={i**2}")

    #[print(f"x={i}, x^2={i**2}") for i in range(1, max+1)]

def zad2(max):
    for i in range(1,max+1):
        if i%2 != 0:
            print(f"x={i}, x^(1/2)={i**(1/2)}")

    #[print((f"x={i}, x^(1/2)={i**(1/2)}")) if i%2 != 0 else None for i in range(1,max+1)]

def zad3():
    def iloczyn(a, b):
        return a*b
    try:
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        print(f"a * b = {a} * {b} = {iloczyn(a, b)}")
    except:
        print("To nie liczba!")
        zad3()

if __name__ == "__main__":
    print("\nZad 1\n**************")
    zad1(10)

    print("\nZad 2\n**************")
    zad2(9)

    print("\nZad 3\n**************")
    zad3()