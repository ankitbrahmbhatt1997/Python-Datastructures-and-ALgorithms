def solution(N):
    factorCount = 0
    i = 1
   
    while i*i < N:
       
        if N%i == 0:
            factorCount+=2
           
        i+=1

    if i*i == N:
        factorCount+=1
    

    return factorCount


print(solution(2))
