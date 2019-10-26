from sys import stdin



t = int(stdin.readline())

for _ in range(t):
    N,M = map(int,stdin.readline().strip().split(" "))
    A = list(map(int,stdin.readline().strip().split(" ")))
    iterationCounter = 1
    catCount = 0
    cats = {}
    ans = ""
    for i in range(1,N+1):
        cats[i] = 0
    for i in A:
        if cats[i] == iterationCounter-1:
            cats[i] = cats[i]+1
            catCount+=1
            if catCount == N:
                catCount = 0
                iterationCounter+=1
        else:
            ans = "NO"
            break
        
    if ans == "":
        ans = "YES"
    print(ans)

        
