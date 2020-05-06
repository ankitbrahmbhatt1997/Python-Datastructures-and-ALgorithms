def solution(X, Y, D):

    numberOfJumps = (Y-X)/D
    afterDecimal = str(numberOfJumps).split(".")[1]
    
    if int(afterDecimal) > 0:
        numberOfJumps = int(numberOfJumps) +1
    return int(numberOfJumps)
    

print(solution(0,60,60))
