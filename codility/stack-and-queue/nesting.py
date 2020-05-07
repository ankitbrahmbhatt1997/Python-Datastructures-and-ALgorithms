def solution(S):

    stack = []

    for i in S:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            else:
                lastElement = stack.pop()
                

    if len(stack) != 0:
        return 0
    return 1
