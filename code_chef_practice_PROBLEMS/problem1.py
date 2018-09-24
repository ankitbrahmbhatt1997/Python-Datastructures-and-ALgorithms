t = int(input())

for i in range(t):
    n, c = map(int, input().strip().split(" "))
    individual_candies = list(map(int, input().strip().split(" ")))
    sum = 0
    for i in individual_candies:
        sum = sum+i
    if sum <= c:
        print("Yes")
    else:
        print("No")
