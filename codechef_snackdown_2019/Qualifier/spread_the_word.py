from sys import stdin
t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    people = 1+arr[0]
    prev = 1
    days = 1
    prev_sum = arr[0]
    while people < n:
        sum = 0
        for j in range(prev, people):
            sum = sum+arr[j]
        sum += prev_sum
        prev_sum = sum
        prev = people
        people += sum
        days += 1
    print(days)
