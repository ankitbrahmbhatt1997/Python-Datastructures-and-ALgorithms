def solution(A):
    if len(A) == 0:
        return 0
    
    max_num = sum = A[0]
    
    for n in A[1:]:
        sum = max(sum+n, n)
        max_num = max(sum, max_num)
    return max_num



print(solution([1,1]))