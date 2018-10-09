from sys import stdin
t = int(stdin.readline())
for i in range(t):
    N, K, Q = map(int, stdin.readline().strip().split(" "))
    S = stdin.readline()
    for i in range(Q):
        lower, upper = map(int, stdin.readline().strip().split(" "))
        required_string = S[lower-1:upper]

        count = 0
        for j in range(0, len(required_string)):
            ones = 0
            zeros = 0
            if required_string[j] == "1":
                ones += 1
            else:
                zeros += 1
            z = j
            while ones <= K and zeros <= K and z < len(required_string)-1:
                z += 1
                if required_string[z] == "1":
                    ones += 1
                else:
                    zeros += 1
                if ones <= K and zeros <= K:
                    count += 1
                else:
                    break
        print(len(required_string)+count)
