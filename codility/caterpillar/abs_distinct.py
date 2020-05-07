def solution(A):
    distinct = set()
    for i in A:
        if i < 0:
            distinct.add(-i)
        else:
            distinct.add(i)

    return len(distinct)



print(solution([-5,-3,-1,0,3,6,6,7,0,-7,-5,-3,-8]))
