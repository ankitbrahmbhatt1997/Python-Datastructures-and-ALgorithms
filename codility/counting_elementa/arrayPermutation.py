def solution(A):
    presentNumbers = set()
    count = 0
    for i in A:
        presentNumbers.add(i)
    
    for i in range(1,len(A)+1):
        if i not in presentNumbers:
            return 0
        

    return 1


print(solution([4,1,3]))