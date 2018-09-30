from sys import stdin

t = int(stdin.readline())

for i in range(t):
    N = int(stdin.readline())
    cars = list(map(int, stdin.readline().strip().split(" ")))
    ordered_cars = []
    alley = []
    check = 1
    ns = 1
    k = 0
    while len(cars) > 0:

        if cars[0] == check:
            check += 1
            ordered_cars.append(cars.pop(0))
        else:

            if len(alley) == 0:
                alley.append(cars.pop(0))
            elif alley[-1] > cars[0]:

                alley.append(cars.pop(0))

            elif alley[-1] < cars[0]:

                while alley[-1] < cars[0]:

                    if alley[-1] == check:

                        ordered_cars.append(alley.pop())
                        check += 1
                    else:
                        print("no")
                        ns = 0
                        break
                    if len(alley) == 0:
                        break
                if len(alley) != 0:
                    if alley[-1] > cars[0]:
                        alley.append(cars.pop(0))
                if ns == 0:
                    break

    if len(cars) == 0 and len(alley) != 0:
        while len(alley) > 0:
            ordered_cars.append(alley.pop())

        print("yes")
