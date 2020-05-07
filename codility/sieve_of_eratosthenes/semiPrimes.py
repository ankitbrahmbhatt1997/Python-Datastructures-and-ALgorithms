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

def solution(N, P, Q):

    sieve = pre_factorization(N)
    semiPrimes = [0] * (N+1)
    # calculating semi primes
    for k in range(1,len(sieve)):
            if sieve[k] > 0:
                remaining = k//sieve[k]
                if sieve[remaining] == 0:
                    semiPrimes[k] = 1


    prefix = []
    prefix.append(0) 
    prefix.append(0) 
    prefix.append(0) 
    prefix.append(0) 
    prefix.append(1)

    for i in range(5,N+1):
        prefix+= [prefix[-1]+ semiPrimes[i]]

    
           

    # print(semiPrimes)

    answers = []
    for i,j in zip(P,Q):
        
        answers+=[prefix[j]-prefix[i-1]]

    return answers



print(solution(26,[1,4,16],[26,10,20]))
