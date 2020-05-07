def solution(K, A):
    count = 0
    ropeLength = 0
    for i in A:
        
        ropeLength+=i
        if ropeLength >= K:
            count+=1
            ropeLength = 0

    return count

print(solution(4,[1,1,1,1,1,1]))


