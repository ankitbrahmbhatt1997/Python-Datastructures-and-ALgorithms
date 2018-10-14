

from sys import stdin
t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    A = list(map(int, stdin.readline().strip().split(" ")))
    B = list(map(int, stdin.readline().strip().split(" ")))
    c = 0
    result = ""
    while c < len(A)-3:
        d = 1
        j = c
        while j < len(A)-1:
            if A[j] < B[j]:
                A[j] += d
                d += 1
                if A[j] == B[j]:
                    c += 1
            elif A[j] == B[j]:
                c += 1
            elif A[j] > B[j]:
                result = "N"

        if result == "N":
            break

    if A == B:
        print("TAK")
    else:
        print("NIE")
