def solution(N, A):
    counters = [0] * N
    maxCounter = 0
    for i in A:
        if i <= N:
            
            counters[i-1] +=1
            maxCounter = max(maxCounter,counters[i-1])
        elif i == N+1:
            
            counters = [maxCounter] * N
            

    return counters


print(solution(5,[3,4,4,6,1,4,4]))
        

        




