def pre_factorization(n):
    sieve = [0]*(n+1)
    i=2
    while i*i <= n:
        if sieve[i] == 0:
            if sieve[i] == 0:
                k = i*i
                while k <= n:
                    if sieve[k] == 0:

                        sieve[k] = i
                    k+=i
        i+=1

    return sieve

def factorization(n):
    preFactorizedArray = pre_factorization(n)
    primeFactors = set()
    while preFactorizedArray[n] > 0:
        primeFactors.add(preFactorizedArray[n])
        n //= preFactorizedArray[n]
    primeFactors.add(n)
    return primeFactors






print(factorization(75) )
