def solution(X, A):
    countDict = {}
    count = 0
    time = -1
    for i in range(1,X+1):
        countDict[i] = False

    for i in range(0,len(A)):
        if A[i] in countDict and countDict[A[i]] == False:
            countDict[A[i]]  = True
            count+=1
        if count == X:
            time = i
            break;
    return time

print(solution(5,[1,3,1,4,2,3,5,4]))

            
