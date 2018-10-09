from sys import stdin
N, D = map(int, stdin.readline().strip().split(" "))
arr = []
for i in range(N):
    arr.append(int(stdin.readline()))
arr.sort()
pairs = 0
c = 0
while c < len(arr)-1:
    if (arr[c+1]-arr[c]) <= D:
        pairs += 1
        c += 2
    else:
        c += 1
print(pairs)
