'''
Generate the list of prime factors for a given n. Example prime factors of 12: 2, 2, 3
'''
from genPrimes import Primes

def primeFactorize(n):
    primes = Primes(n)
    primeList = primes.getPrimeList()
    res = []
    while n != 1:
        for p in primeList:
            if n % p == 0:
                res.append(p)
                n = n/p
    return res

print(primeFactorize(645321))
