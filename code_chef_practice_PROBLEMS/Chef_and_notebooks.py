from sys import stdin
t = int(stdin.readline())

for i in range(t):
    x, y, k, n = map(int, stdin.readline().strip().split(" "))
    prices_set = set()
    for j in range(n):
        prices_set.add(tuple(map(int, stdin.readline().strip().split(" "))))
    Required_pages = x-y

    lucky_count = 0
    for l in prices_set:
        if l[0] >= Required_pages and l[1] <= k:

            print("LuckyChef")
            break

    else:
        print("UnluckyChef")
