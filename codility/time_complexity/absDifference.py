import math
def solution(A):
    sum = 0
    for i in A:
        sum+=i
    
    leftSum = 0
    rightSum = sum
    absDiff = math.inf
    for i in A:
        leftSum+=i
        rightSum-=i
        absDiff = min(absDiff,abs(rightSum-leftSum))
    return absDiff

print(solution([-2000,1000]))
