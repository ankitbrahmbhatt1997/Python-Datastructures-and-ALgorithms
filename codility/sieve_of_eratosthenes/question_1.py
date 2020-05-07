def countDivisors(N):
    factors = []
    i = 1
   
    while i*i < N:
       
        if N%i == 0:
            factors.append(i)
            factors.append(N//i)
            
           
        i+=1

    if i*i == N:
        factors.append(i)

    return factors

def solution(A):
    checkList = {}
    appeared = {}
    for i in A:
        if i in checkList:
            checkList[i]+=1
        else:
            checkList[i] = 1
    nonDivisors = []
    for i in A:
        divisors = []
        if i in appeared:
            divisors = appeared[i]
        else:
            divisors = countDivisors(i)
            appeared[i]  = divisors


            
        divisorCount = 0
        for j in divisors:

            if j in checkList:
                divisorCount+=(checkList[j])
        
        
        nonDivisors+= [len(A)-divisorCount]
    
    return nonDivisors


    
    


print(solution([3,1,2,3,6]))