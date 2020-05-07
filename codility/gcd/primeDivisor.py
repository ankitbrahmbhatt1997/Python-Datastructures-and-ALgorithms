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

def solution(A,B):
    count = 0
    for a,b in zip(A,B):
        factorsA = factorization(a)
        factorsB = factorization(b)
        if factorsA.issubset(factorsB) and factorsB.issubset(factorsA):
            count+=1
    
    return count

print(solution([15,10,3],[75,30,5]))


