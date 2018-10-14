from sys import stdin
import bisect
t = int(stdin.readline())

for i in range(t):
    n, k, c = map(int, stdin.readline().strip().split(" "))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    arr.sort()
    c = 0
    while len(arr) >= k:
        count_array = []
        count_array.append(arr[c])
        index = bisect.bisect_left(arr, arr[c]*c)
