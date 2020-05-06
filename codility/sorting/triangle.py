def isTriangle(a,b,c):
    return a+b > c and b+c > a and a+c > b


def solution(A):

    A.sort()
    length = len(A)
    if length < 3:
        return 0
    check = False
    if length%2 == 0:
        index = int(length/2)-1
        # print(index)
        check1 = isTriangle(A[index],A[(index)+1],A[(index)+2])
        check2 = isTriangle(A[index],A[(index)+1],A[(index)-1])
        check =  check1 or check2
    else:
        index = int(length/2)-1
        check3 = isTriangle(A[index],A[index-1],A[index+1])
        check = check3

    if check: return 1 
    else: return 0

print(solution([10,50,5,1]))




