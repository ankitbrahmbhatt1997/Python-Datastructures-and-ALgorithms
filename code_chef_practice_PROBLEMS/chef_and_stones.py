from sys import stdin
t = int(stdin.readline())
for i in range(t):
    n1, n2, d = map(int, stdin.readline().strip().split(" "))
    if d == max(n1, n2, d):
        print(abs(n1-n2))
    else:
        for k in range(d, 0, -1):
            if n1 == 0 or n2 == 0:
                break
            else:
                if k > min(n1, n2):
                    continue
                else:
                    n1, n2 = n1-k, n2-k

        print(n1+n2)
