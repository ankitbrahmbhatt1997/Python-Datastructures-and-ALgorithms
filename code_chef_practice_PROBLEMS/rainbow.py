from sys import stdin
t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    A = list(map(int, stdin.readline().strip().split(" ")))
    result = 1
    for k in range(1, 8):
        if k not in A:
            result = 0

    if result == 1:
        count = {}
        current_number = 1
        current_count = 0
        while current_number < 7:
            if current_number == A[current_count]:
                if current_number in count:
                    count[current_number] += 1
                else:
                    count[current_number] = 1
                current_count += 1
            else:
                current_number = A[current_count]
