def solution(A):
    pairs = {}
    for i in A:
        if i not in pairs:
            
            pairs[i] = False
        elif i in pairs and pairs[i] == False:
            
            
            pairs[i] = True
        elif i in pairs and pairs[i] == True:
            
            
            pairs[i] = False

    

    for i in pairs:
        if pairs[i] == False:
            return i

print(solution([9,3,9,3,9,7,9]))