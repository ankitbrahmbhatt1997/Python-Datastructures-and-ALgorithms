from sys import stdin
t = int(stdin.readline())
for i in range(t):
    str = stdin.readline().strip()
    left = []
    right = []
    dic = {}
    n = len(str)

    if n % 2 == 0:
        left = str[:n//2]
        right = str[n//2:]
    else:
        left = str[:n//2]
        right = str[n//2+1:]

    for j in left:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
    for k in right:
        if k in dic:
            dic[k] -= 1
        else:
            dic[k] = 1

    for j in dic:
        if dic[j] != 0:
            print("NO")
            break
    else:
        print("YES")
