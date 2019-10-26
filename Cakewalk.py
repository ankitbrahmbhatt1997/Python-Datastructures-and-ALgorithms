from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    if n%200 == 0:
        print("Yes")
    else:
        print("NO")