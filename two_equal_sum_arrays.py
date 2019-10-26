from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    A,B,C = map(int,stdin.readline().strip().split(" "))
    input_array = []
    for i in range(A):
        input_array.append(1)
    for i in range(B):
        input_array.append(2)
    for i in range(C):
        input_array.append(3)
    left_sum = 0
    for i in input_array:
        left_sum+=i
   
    right_sum = 0
    N= len(input_array)
    if left_sum % 2 != 0:
        print('NO')
    else:
        for i in range(N-1,-1,-1):
        
        
            if left_sum == right_sum:
                break

            right_sum+=input_array[i]
            left_sum-=input_array[i]
            
            if right_sum > left_sum:
                left_sum+=input_array[i]
                right_sum-=input_array[i]
                
        
        
        
     

        if left_sum == right_sum:
            
            print("YES")
        else:
            print("NO")
        
    

    

        

 
    
