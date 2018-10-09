from sys import stdin
import bisect
t = int(stdin.readline())
for i in range(t):
    N, Q = map(int, stdin.readline().strip().split(" "))
    snakes = list(map(int, stdin.readline().strip().split(" ")))
    snakes.sort()
    for j in range(Q):
        K = int(stdin.readline())
        c = len(snakes)
        while c-1 > 0:
            c = bisect.bisect_right(snakes, K-1)
            if c-2 >= 0:

                snakes[c-1] = snakes[c-1]+1
                del snakes[c-2]
            else:
                break
        count = 0

        for z in snakes:
            if z >= K:
                count += 1
        print(count)
