from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    N,M,Q = map(int,stdin.readline().strip().split(" "))
    Rows = {}
    Columns = {}
    
    for i in range(Q):
        row,column = map(int,stdin.readline().strip().split(" "))
        if row in Rows:
            Rows[row]+=1
        else:
            Rows[row] = 1
        if column in Columns:
            Columns[column]+=1
        else:
            Columns[column] = 1
    odd_count = 0
    for col in Columns:
        if Columns[col] % 2 == 0:
            continue
        odd_count+=1

    
    count = 0      
    for i in range(N):
        row_value = 0
        if i+1 in Rows:
            row_value = Rows[i+1]
        if row_value % 2 == 0:
            count+=odd_count
        else:
            count+=M-odd_count
    
    print(count)

