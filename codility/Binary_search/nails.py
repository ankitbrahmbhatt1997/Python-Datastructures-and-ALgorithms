def solution(A,B,C):
    planksNailed = 0
    nails = [0] * len(C)
    C.sort()
    for a,b in zip (A,B):

        for i in range(0,len(C)):
            if a <= C[i] <= b:
                planksNailed+=1
                nails[i]

        # lower = 0
        # upper = len(C) - 1
        # while lower < upper:
        #     # print(lower,upper)
        #     print(a,b)
            
        #     mid = (upper+lower)//2
        #     # print(mid)
        #     if a <= C[mid] <= b:
        #         print(True)
        #         planksNailed +=1
        #         nails[mid] = 1
        #         break
            
        #     elif C[mid] > b:
        #         upper = mid-1

        #     elif C[mid] < a:
        #         lower = mid+1

    print(planksNailed)
    print(nails)


print(solution([1,4,5,8],[4,5,9,10],[4,6,7,10,2]))