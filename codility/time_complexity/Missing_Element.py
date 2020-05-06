

def solution(A):
    N = len(A)
    totalSum = 0
    for i in range(1,N+2):
        totalSum+=i
    givenSum = 0
    for i in A:
        givenSum+=i

    return totalSum - givenSum

print(solution([2,3,1,5,4]))
