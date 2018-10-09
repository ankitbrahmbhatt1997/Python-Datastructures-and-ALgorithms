from sys import stdin
import bisect
t = int(stdin.readline())
for i in range(t):
    n = int(map(str, stdin.readline()))
    arr = list(map(int, stdin.readline().strip().split(" ")))

    st = []
    for j in arr:
        index = bisect.bisect_left(st, j+1)

        if index == len(st):
            st.append(j)
        else:
            st[index] = j

    print(len(st), end=" ")
    for z in st:
        print(z, end=" ")
