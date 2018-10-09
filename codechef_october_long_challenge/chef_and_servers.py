from sys import stdin
t = int(stdin.readline())
for i in range(t):
    p1, p2, k = map(int, stdin.readline().strip().split(" "))
    if p1+p2 < k:
        print("CHEF")
    else:
        if (p1+p2) % k == 0:
            value = (p1+p2)/k
            if value % 2 == 0:
                print("CHEF")
            else:
                print("COOK")
        else:
            value = ((p1+p2) - ((p1+p2) % k))/k
            if value % 2 == 0:
                print("CHEF")
            else:
                print("COOK")
