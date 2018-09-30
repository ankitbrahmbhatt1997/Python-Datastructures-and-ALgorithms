from sys import stdin


def squares(b):
    sq = 0
    if b-2 < 2:
        return 0
    while b-2 >= 2:
        sq = sq+((b-2)//2)
        b -= 2
    return sq


t = int(stdin.readline())

for i in range(t):
    print(squares(int(input())))
