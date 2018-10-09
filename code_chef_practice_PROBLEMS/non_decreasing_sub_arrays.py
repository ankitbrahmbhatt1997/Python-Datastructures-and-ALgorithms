from sys import stdin
t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    dp = [1]*n
    for j in range(n-1, 0, -1):
        if arr[j] >= arr[j-1]:
            dp[j-1] += dp[j]
        else:
            continue

    print(sum(dp))
