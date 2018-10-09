from sys import stdin
t = int(stdin.readline())
for i in range(t):
    N, K = map(int, stdin.readline().strip().split(" "))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    c = 0
    for k in arr:
        if (k+K) % 7 == 0:
            c += 1

    print(c)
