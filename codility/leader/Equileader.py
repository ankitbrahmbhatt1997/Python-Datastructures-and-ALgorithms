def solution(A):

    stack = []
    candidate = 0
    n = len(A)
    for i in A:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.append(i)
            else:
                stack.pop()

    if len(stack) == 0:
        return 0
    candidate = stack[-1]
    leader = 0
    leaderIndex = 0
    count = 0
    for i in A:
        if i == candidate:
            count+=1
    if count >= (n//2)+1:
        leader = candidate
        leaderIndex = A.index(candidate)

    S = 0
    leftCount = 0
    rightCount = count
    for i in range(0,n):
        length = i+1
        if A[i] == leader:
            leftCount+=1
            rightCount-=1

        if leftCount >= (length//2)+1 and rightCount >= ((n-length)//2)+1:
            S+=1

    return S
            


print(solution([4,3,4,4,4,2]))