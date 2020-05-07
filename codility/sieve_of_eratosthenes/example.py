# Finding all the prime number between 2 and n


def findingPrimes(n):
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False
    i=2
    while i*i <= n:
        if sieve[i]:
            k = i*i
            while k <= n:
                sieve[k] = False
                k+=i
        i+=1

    return sieve





print(findingPrimes(17))