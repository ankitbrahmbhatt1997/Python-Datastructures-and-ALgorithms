from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    N = int(stdin.readline())
    prices = list(map(int,stdin.readline().strip().split(" ")))
    min_val = prices[0]
    c=1
    count=1
    for i in range(1,N):
        if c > 5:
            min_val = min(prices[i-5:i])
        if prices[i] < min_val:
            count+=1
            min_val = prices[i]
        c+=1
    print(count)