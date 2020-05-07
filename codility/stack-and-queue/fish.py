def solution(A, B):

    fishStack = []

    for a,b in zip(A,B):
        if len(fishStack) == 0:
            fishStack.append((a,b))
        else:
            if fishStack[-1][1] == 0:
                fishStack.append((a,b))
            else:
                if b == 1:
                    fishStack.append((a,b))
                else:
                    lastElement = fishStack.pop()
                    if lastElement[0] > a:
                        fishStack.append(lastElement)
                    else:
                        fishStack.append((a,b))


    # print(fishStack)
    return len(fishStack)


print(solution([4,3,5,1,2],[1,1,0,1,1]))