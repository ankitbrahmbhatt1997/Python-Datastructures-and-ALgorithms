def solution(A, B):

    maxCount = 0
    for i in range(len(A)-1,-1,-1):
        currentCount = 1
        for j in range(i-1,-1,-1):
            if A[j] <= A[i] <= B[j]:
                continue
            else:
                currentCount+=1

        print(currentCount)


solution([1,3,7,9,9],[5,6,8,9,10])

        

