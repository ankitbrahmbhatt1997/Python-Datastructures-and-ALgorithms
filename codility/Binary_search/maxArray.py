
def isBlockSizePossible(A,K,tentativeBlockSum):
    blockSum=0
    blockCount=0

    for i in A:
        if blockSum + i > tentativeBlockSum:
            blockSum = i
            blockCount+=1
        else:
            blockSum+=i
        if blockCount >= K:
            return False
    
    return True






def solution(K,M,A):
    lower = max(A)
    upper = sum(A)

    if K == 1: return upper
    if K >= len(A): return lower

    while lower <= upper:
        mid = (upper+lower)//2
        if isBlockSizePossible(A,K,mid):
            upper = mid-1
        else:
            lower = mid+1
    return lower



print(solution(3,5,[2,1,5,1,2,2,2]))


        