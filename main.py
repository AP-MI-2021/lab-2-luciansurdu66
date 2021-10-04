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
            j+=1
        return primes
def odd_primes(N):
    '''

    :param N:
    :return:
    '''
    oddprimes = Eratostene(N)
    oddprimes.remove(2)
    return(oddprimes)

def get_goldbach(n):
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
def test_get_goldbach()

if __name__ == "__main__":
    n =int(input("Dati un numar"))
    p1,p2 = get_goldbach(n)
    print(p1,p2)
