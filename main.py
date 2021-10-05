def Eratostene(n):
    '''
    determină Ciurul lui Eratostene
    :param n: nr. întreg
    :return: numerele prime cu ajutorul Ciurului lui Eratostene
    '''
    primes = list(range (2,n+1))
    for i in primes:
        j=2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
        return primes
def odd_primes(N):
    oddprimes = Eratostene(N)
    oddprimes.remove(2)
    return(oddprimes)

def get_goldbach(n):
    '''
    verifica conjectura lui Goldbach
    :param n: nr. intreg
    :return:cel mai mic si cel mai mare numar prim a caror suma este egala cu n
    '''
    x,y = 0, 0
    rezultat = 0
    if n%2 == 0:
        prime = odd_primes(n)
        while rezultat !=n:
            for i in range(len(prime)):
                if rezultat == n: break
                x=prime[i]
                for j in range(len(prime)):
                    y=prime[j]
                    rezultat = x+y
                    if rezultat == n: break
    return x,y
def get_newton_sqrt(n,steps):
    """
    Calculeaza rădăcina pătrată
    :param n: nr real
    :param steps: nr intreg
    :return: rădăcina numărului
    """
    x= float(n)
    for i in range(steps):
        n = 0.5 * (n + x / n)
    return n
def test_get_newton_sqrt():
    assert get_newton_sqrt(81,8) == 9.0
    assert get_newton_sqrt(5,6) == 2.23606797749979
shouldRun = True
while shouldRun:
    print("1. Determină numerele prime p1 și p2 astfel astfel încât n=p1+p2, p1 minim și p2 maxim")
    print("2. Determinati daca un nr. este prim")
    print("x. Iesire")
    optiune = input("Dati opțiunea: ")
    if optiune == "1":
        n= int(input('Dați un număr par >2 : '))
        p1, p2 = get_goldbach(n)
        print(p1,p2)
    elif optiune == "2":
        test_get_newton_sqrt()
        x = int(input("Dați un nr."))
        steps = int(input("Dați un număr de pași: "))
        print("Rădăcina numărului este: ",get_newton_sqrt(x,steps))
    elif optiune == "x":
        shouldRun = False
    else:
        print("Opțiune greșită! Reincercați!")
