def solution(A):
    nz = 0
    count = 0
    for i in A:
        if i == 0:
            nz+=1
        elif i == 1:
            count+=nz

    if count <= 1000000000:
        return count
    else:
        return -1

print(solution([0,1,0,1,1]))