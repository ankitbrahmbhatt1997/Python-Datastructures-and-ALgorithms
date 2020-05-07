def solution(N):
    factorCount = 0
    factors = []
    i = 1
   
    while i*i < N:
       
        if N%i == 0:
            factors.append((i,N//i))
            
           
        i+=1

    if i*i == N:
        factors.append((i,N//i))

    minPerameter = float("inf")

    for pairs in factors:
        currentParameter = 2*(pairs[0]+pairs[1])
        minPerameter = min(minPerameter,currentParameter)


    return minPerameter

print(solution(30))  
    