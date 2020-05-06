def solution(A, K):
    arrayLength = len(A)
    newArray = A[:]
    for i in range(0,arrayLength):
        newPosition = i+K
        if newPosition >= arrayLength:
            newPosition = newPosition % arrayLength
        newArray[newPosition] = A[i]

    return newArray



print(solution([1, 2, 3, 4],4))



