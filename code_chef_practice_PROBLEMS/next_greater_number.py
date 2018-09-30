
t = int(input())

for i in range(t):
    m = int(input())
    if 1 <= m <= 1000000:

        numbers = list(map(int, input().strip().split(" ")))
        suffix = []
        start = numbers.pop()
        suffix.insert(0, start)
        while numbers[-1] >= suffix[0]:
            suffix.insert(0, numbers.pop())
            if(len(numbers) == 0):
                break
        if(len(numbers) == 0):
            print("-1")
        else:

            for i in range(len(suffix)-1, -1, -1):
                if numbers[-1] < suffix[i]:
                    temp = numbers[-1]
                    numbers[-1] = suffix[i]
                    suffix[i] = temp
                    break

            while len(suffix) > 0:
                numbers.append(suffix.pop())

            s = ""
            for i in numbers:
                s = s+str(i)
            print(s)
