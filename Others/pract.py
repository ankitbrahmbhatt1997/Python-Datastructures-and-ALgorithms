from sys import stdin

for _ in range(0, 5):
    input_list = list(map(int, stdin.readline().strip().split(" ")))
    unique_count = {}
    output_list = []
    unique_count[input_list[0]] = 1
    output_list.append(input_list[0])
    for i in input_list:
        if i in unique_count:
            continue
        else:
            unique_count[i] = 1
            output_list.append(i)
    output_list.sort()
    for x in output_list:
        print(x, end=" ")
    print()
