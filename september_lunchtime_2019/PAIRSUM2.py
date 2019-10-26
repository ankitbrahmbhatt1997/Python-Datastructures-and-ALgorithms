from sys import stdin



t = int(stdin.readline())

for _ in range(t):
    N,Q = map(int,stdin.readline().strip().split(" "))
    B = list(map(int,stdin.readline().strip().split(" ")))
    evaluated = []
    positive = 1
    sum = 0
    for i in range(N-1):
        sum+=B[i]*positive
        evaluated.append(sum)           
        positive = positive * -1

    for i in range(Q):
        p,q = map(int,stdin.readline().strip().split(" "))
        if abs(p-q)%2 == 0:
            print("UNKNOWN")
        else:
            minValue = 0
            maxValue = 0
            if p > q:
                minValue = q
                maxValue = p
            else:
                
                minValue = p
                maxValue = q
            if abs(p-q) == 1:
                
                print(B[minValue-1])
            else:
                print(evaluated[maxValue-2])
                    
                    
                

