from sys import stdin
t = int(stdin.readline())

for i in range(t):
    n, k = map(int, stdin.readline().strip().split(" "))
    forgotten = stdin.readline().strip().split(" ")

    phrases = ""
    for z in range(k):
        s = stdin.readline().strip()
        phrases = phrases+" "+s

    for y in forgotten:
        if y in phrases:
            print("YES", end=" ")
        else:
            print("NO", end=" ")
