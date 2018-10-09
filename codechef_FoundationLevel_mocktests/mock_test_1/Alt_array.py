from sys import stdin


def oppSign(x, y):
    return (x ^ y) < 0


t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    dp = [1]*n
    for j in range(n-2, -1, -1):

        if oppSign(arr[j], arr[j+1]):
            dp[j] = dp[j+1]+1

    for z in dp:
        print(z, end=" ")
