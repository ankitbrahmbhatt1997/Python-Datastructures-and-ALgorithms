from sys import stdin
t = int(stdin.readline())
for i in range(t):
    N, K = map(int, stdin.readline().strip().split(" "))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    arr.sort()
    new_arr = arr[K:N-K]

    avg = sum(new_arr)/len(new_arr)
    print(str.format("{0:.6f}", avg))
