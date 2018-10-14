from sys import stdin
t = int(stdin.readline())
for i in range(t):
    n, k = map(int, stdin.readline().strip().split(" "))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    arr.sort(reverse=True)
    team_count = 1
    prev = arr[0]
    unique = 1
    while team_count < len(arr):
        if unique == k:
            break
        else:
            if arr[team_count] != prev:
                prev = arr[team_count]
                team_count += 1
                unique += 1

            else:
                team_count += 1
    print(team_count)
