from sys import stdin


def swap(str):
    if str == "R":
        return "G"
    else:
        return "R"


t = int(stdin.readline())
for i in range(t):
    N, K = map(int, stdin.readline().strip().split(" "))
    colors = list(map(str, stdin.readline().strip()))
    steps = 0
    for j in range(0, N):

        if colors[j] == 'R':

            steps += 1
            limit = min(N-1, j+K-1)

            c = j
            while(c <= limit):
                swapped = swap(colors[c])

                colors[c] = swapped
                c += 1

        else:
            continue
    print(steps)
