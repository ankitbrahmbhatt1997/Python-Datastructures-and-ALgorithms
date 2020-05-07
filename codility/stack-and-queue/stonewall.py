def solution(H):
    
    blockCount = 0

    stack = []
    for i in H:
        if len(stack) == 0:
            stack.append(i)
            blockCount+=1
        else:
            if stack[-1] == i:
                continue
            elif stack[-1] < i:
                blockCount+=1
                stack.append(i)
            elif stack[-1] > i:
                
                while len(stack) != 0:
                    
                    if stack[-1] == i:
                        break
                    elif stack[-1] < i:
                        stack.append(i)
                        blockCount+=1
                        break
                    stack.pop()
                else:
                    stack.append(i)
                    blockCount+=1
    
    return blockCount

print(solution([2, 5, 1, 4, 6, 7, 9, 10, 1]))

