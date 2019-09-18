from sys import stdin
from heapq import heapify,heappop,heappush




def cookies(K,A):
    
    heapify(A)
    count=0
    while len(A) > 0:
        least_sweetness = heappop(A)
        if len(A) == 1 and A[0] < K :
            return -1
        if least_sweetness > K:
            return count
        second_least_sweetness = heappop(A)
        count+=1
        heappush(A,(least_sweetness+2*second_least_sweetness))
        





N,K = map(int,stdin.readline().strip().split(" "))
sweetness_values = list(map(int,stdin.readline().strip().split(" ")))
print(cookies(K,sweetness_values))
