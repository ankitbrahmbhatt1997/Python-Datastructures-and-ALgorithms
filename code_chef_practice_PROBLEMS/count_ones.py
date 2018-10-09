from sys import stdin
t = int(stdin.readline())

for i in range(t):
    st = stdin.readline().strip()
    ones = []
    c = 0
    for j in range(0, len(st)):
        if st[j] == "1":
            ones.append(j)

    if len(ones) > 0:
        for j in range(0, len(ones)-1):
            if ones[j] != ones[j+1] - 1:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
