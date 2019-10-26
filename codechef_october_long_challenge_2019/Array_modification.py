try:
    from sys import stdin

    t = int(stdin.readline())





    for _ in range(t):
    
        N,K = map(int,stdin.readline().strip().split(" "))
        sequence = list(map(int,stdin.readline().strip().split(" ")))




        perfect_loops = K//N
        rem = K%N
        if K < N:
            perfect_loops = 0
            rem = K

        new_sequence = [0 for i in range(N)]

  
    

        for i in range(N):

            
            iterations = perfect_loops
            if i < rem:
                iterations+=1
            a= sequence[i]
            b =sequence[N-(i)-1]
            c = a^b
            selected_value = 1 + (iterations % 3)
            if N%2==1 and i == N-(i)-1 and selected_value > 1:
                new_sequence[i] = 0    
                continue
    
            if i < N//2:
                if selected_value == 1:
                    new_sequence[i] = a
           

                elif selected_value == 2:
                    new_sequence[i] = c
            
                    
            
                elif selected_value == 3:
                    new_sequence[i] = b
        
            else:
                if selected_value == 1:
                    new_sequence[i] = a
           

                elif selected_value == 2:
                    new_sequence[i] = b
            
                    
            
                elif selected_value == 3:
                    new_sequence[i] = c


        
            
        


        for i in new_sequence:
            print(i,end=" ")


except:
    pass




