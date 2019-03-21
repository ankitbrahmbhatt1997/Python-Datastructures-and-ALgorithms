# from itertools import combinations
# from sys import stdin

# t = int(stdin.readline())
# for _ in range(t):
#     N, K1, K2, K3 = map(int, stdin.readline().strip().split(" "))
#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     sum_array = []
#     for i in range(N):
#         sum_array.append(set(combinations(arr, i+1)))
#     print(sum_array)


t=int(input())
while(t>0):
    t-=1
    n,k1,k2,k3=map(int,input().split())
    arr=list(map(int,input().split()))
    add=[]
    for i in range(len(arr)):
        su=arr[i]
        add.append(su)
        for j in range(i+1,len(arr)):
            su+=arr[j]
            add.append(su)
    add.sort(reverse=True)
    print(add[k1-1],add[k2-1],add[k3-1])
            