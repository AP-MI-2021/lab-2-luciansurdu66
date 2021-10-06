def eratostene(n, isPrime):
    '''
    determină Ciurul lui Eratostene
    :param n: nr. întreg
    :return: numerele prime cu ajutorul Ciurului lui Eratostene
    '''
    isPrime[0] = isPrime[1] = False
    for i in range(2, n + 1):
        isPrime[i] = True
    p = 2
    while (p * p <= n):
        if isPrime[p]:
            i = p * p
            while (i <= n):
                isPrime[i] = False
                i += p
        p += 1


def get_goldbach(n):
    '''
    verifica conjectura lui Goldbach
    :param n: nr. intreg
    :return:cel mai mic si cel mai mare numar prim a caror suma este egala cu n
    '''
    x, y = 0, 0
    i = 0
    isPrime = [0] * (n + 1)
    eratostene(n, isPrime)
    for i in range(0, n):
        if (isPrime[i] and isPrime[n - i]):
            break
    x = i
    y = n-i
    return x, y


def test_get_goldbach():
    assert get_goldbach(100) == (3, 97)
    assert get_goldbach(32) == (3, 29)


def get_newton_sqrt(n, steps):
    """
    Calculeaza rădăcina pătrată
    :param n: nr real
    :param steps: nr intreg
    :return: rădăcina numărului
    """
    x = float(n)
    for i in range(steps):
        n = 0.5 * (n + x / n)
    return n


def test_get_newton_sqrt():
    assert get_newton_sqrt(81, 8) == 9.0
    assert get_newton_sqrt(5, 6) == 2.23606797749979


def is_superprime(n):
    '''
    Verifica daca un numar este superprim
    :param n: numar intreg
    :return: valoare de adevar in functie de caz
    '''
    copie = n
    if n < 2:
        return False
    elif n % 2 == 0:
        return False
    else:
        while copie != 0:
            for i in range(3, copie//2):
                if n % i == 0:
                    return False
            copie = copie//10
    return True


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(21) is False
    assert is_superprime(37) is True


shouldRun = True
while shouldRun:
    print("1. Determină numerele prime p1 și p2 astfel astfel încât n=p1+p2, p1 minim și p2 maxim")
    print("2. Determinati rădăcina pătrată a unui număr")
    print("3. Determină dacă un nr. este superprim")
    print("x. Iesire")
    optiune = input("Dati opțiunea: ")
    if optiune == "1":
        test_get_goldbach()
        n = int(input('Dați un număr par >2 : '))
        p1, p2 = get_goldbach(n)
        print(p1, p2)
    elif optiune == "2":
        test_get_newton_sqrt()
        x = int(input("Dați un nr."))
        steps = int(input("Dați un număr de pași: "))
        print("Rădăcina numărului este: ", get_newton_sqrt(x, steps))
    elif optiune == "3":
        n = int(input("Dați un nr."))
        if is_superprime(n):
            print(f"Numărul este superprim")
        else:
            print(f"Numărul nu este superprim")
        test_is_superprime()
    elif optiune == "x":
        shouldRun = False
    else:
        print("Opțiune greșită! Reincercați!")
