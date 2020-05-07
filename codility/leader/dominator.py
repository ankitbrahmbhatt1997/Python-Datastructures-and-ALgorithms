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
        return -1

    candidate = stack[-1]
    leader = 0
    count = 0
    for i in A:
        if i == candidate:
            count+=1
    if count >= (n//2)+1:
        leader = A.index(candidate)
    else:
        leader = -1
    return leader



print(solution([3,4,3,2,3,-1,3,3]))