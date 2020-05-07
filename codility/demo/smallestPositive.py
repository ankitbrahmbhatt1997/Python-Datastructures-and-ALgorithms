def solution(A):
    listDict = set()
    for i in A:
        listDict.add(i)
    smallestPositive = 1
    i = 0
    while smallestPositive  in listDict:
        smallestPositive+=1
    return smallestPositive

print(solution([-1,-3]))
