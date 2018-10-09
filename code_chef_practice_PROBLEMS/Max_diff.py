from sys import stdin
t = int(stdin.readline())
for i in range(t):
    n, k = map(int, stdin.readline().strip().split(" "))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    arr.sort()
    c_sum = 0
    T_sum = 0
    if (n-k) < k:
        k = n-k
    for j in range(0, len(arr)):
        if j <= k-1:
            c_sum = c_sum+arr[j]

        else:
            T_sum = T_sum+arr[j]
    print(T_sum-c_sum)
