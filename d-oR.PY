from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    l,r = map(int,stdin.readline().strip().split(" "))
    values = [*range(l,r+1,1)]
    max_or = 0
    print(len(values))
    for i in range(92684):
        for j in range(92684):
            pass
    # for i in range(len(values)):
    #     for j in range(len(values)):
    #         value = values[i] | values[j]
    #         if value > max_or:
    #             max_or = value

    print(max_or)
