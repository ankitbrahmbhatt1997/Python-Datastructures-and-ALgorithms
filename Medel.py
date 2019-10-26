from sys import stdin
from collections import OrderedDict 

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    numbers= list(map(int,stdin.readline().strip().split(" ")))
    num_dict=OrderedDict()
    for i in numbers:
        if i not in num_dict:
            num_dict[i] = True
    
    while len(numbers) >= 3:
        max_value =  max(numbers[0],numbers[1],numbers[2])
        min_value=  min(numbers[0],numbers[1],numbers[2])
        sum_value = sum([numbers[0],numbers[1],numbers[2]])
        median = sum_value-(max_value+min_value)
        numbers.remove(median)

    print(*numbers)



