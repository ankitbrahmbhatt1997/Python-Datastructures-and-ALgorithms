from sys import stdin
t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    arr.sort()
    pair_list = []
    c = 0
    while c < len(arr)-1:
        if arr[c] == arr[c+1]:
            pair_list.append(arr[c])
            c += 2
        else:
            c += 1

    if len(pair_list) < 2:
        print("-1")
    else:
        print(pair_list[-1]*pair_list[-2])
