def solution(A):
    A.sort()
    
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])


print(solution([-5, 5, -5, 4]))

