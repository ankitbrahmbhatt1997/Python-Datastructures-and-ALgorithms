def solution(A, B, K):
    count = 0
    start=0
    end=0
    if A == B:
        if A%K == 0:
            return 1
        return 0
    for i in range(A,B+1):
        if i%K == 0:
            count+=1
            start = i
            break

    i = B
    while i >= start:
        if i%K == 0:
            count+=1
            end = i
            break
        i-=1
    
    remainingCount = int((end-start)/K) - 1
    return count+remainingCount


print(solution(5,5,3))
