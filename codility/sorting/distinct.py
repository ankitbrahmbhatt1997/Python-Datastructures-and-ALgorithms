def solution(A):
    distinct = set()

    count = 0
    for i in A:
        if i not in distinct:
            count+=1
            distinct.add(i)

    return count

print(solution([2,1,1,2,3,1]))