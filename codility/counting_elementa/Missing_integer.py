def solution(A):
    smallestPositive = 1
    presentElements = set()
    for i in A:
        presentElements.add(i)
    
    for i in range(0,len(A)):
        if smallestPositive in presentElements:
            smallestPositive+=1
            continue
        else:
            break
    return smallestPositive


print(solution([-1,-3]))
        