'''
Returneaza true daca n este prim si false daca nu...
'''


def is_prime(n):
    if n < 2:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i = i + 1
        return True


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    p = 1
    for x in lst:
        p = p * x
    return p


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def main():
    finish = False
    while not finish:
        print("1. Verificati daca un numar e prim")
        print("2. Calculati produsul numerelor dintr-o lista")
        print("3. CMMDC (scaderi)")
        print("4. CMMDC (Euclid)")
        print("x. Exit")
        optiune = input()
        if optiune == '1':
            x = int(input())
            print(is_prime(x))
        elif optiune == '2':
            str = input("Introduceti numerele separate prin virgula: ")
            lst = str.split(',')
            for i, x in enumerate(lst):
                lst[i] = int(x)
            print(get_product(lst))
        elif optiune == '3':
            a = int(input())
            b = int(input())
            print(get_cmmdc_v1(a, b))
        elif optiune == '4':
            a = int(input())
            b = int(input())
            print(get_cmmdc_v2(a, b))
        elif optiune == 'x':
            finish = True
        else:
            print("Optiune incorecta")


if __name__ == '__main__':
    main()
