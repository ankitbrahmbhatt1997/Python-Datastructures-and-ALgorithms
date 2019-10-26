from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    A,B = map(int,stdin.readline().strip().split(" "))
    sum = str(A + B)
    matches = {
        "0":6,
        "1":2,
        "2":5,
        "3":5,
        "4":4,
        "5":5,
        "6":6,
        "7":3,
        "8":7,
        "9":6
    }
    required_matches = 0
    for i in sum:
        required_matches+=matches[i]

    print(required_matches)