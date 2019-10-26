from sys import stdin



def calculate(query,A,B):
    identified = False
    if A > query[1]:
        A = query[2]
        B = query[1]
        identified = True
    elif A > query[2]:
        A = query[1]
        B = query[2]
        identified = True

    elif A < query[1] and B > query[2]:
        A = query[2]
        B = query[1]
        identified = True
    elif A < query[2] and B > query[1]:
        A = query[1]
        B = query[2]
        identified = True
    return A,B,identified


t = int(stdin.readline())

for _ in range(t):
    N = int(stdin.readline())
    A,B = 0,0
    for i in range(N):
        query = list(map(int,stdin.readline().strip().split(" ")))
        
        if query[0] == 1:
            A=query[1]
            B = query[2]
            print("YES")
        elif query[0] == 2:
            A1,B1,identified = calculate(query,A,B)
            
            if  query[1] == query[2]:
                print("YES")
                A=B = query[1]
            else:
                if A == A1 and B == B1 and identified == False or i == 0:
                    print("NO")
            
                else:
                    A,B = A1,B1
                    print("YES")

            

        