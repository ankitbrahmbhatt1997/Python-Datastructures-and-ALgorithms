from sys import stdin

t = int(stdin.readline())

fi = open("input.txt","r")



for _ in range(t):
    
    N,K = map(int,stdin.readline().strip().split(" "))
    sequence = list(map(int,fi.readline().strip().split("\t")))




    perfect_loops = K//N
    rem = K%N
    if K < N:
        perfect_loops = 0
        rem = K

    new_sequence = [0 for i in range(N)]
    new_sequence_2 = sequence[:]

    half_loop = N//2 if N%2 == 0 else N//2 +1

    for i in range(K):
        a = new_sequence_2[i%N]
        b = new_sequence_2[N-(i%N)-1]
        new_sequence_2[i%N] = a^b
    

    for i in range(N):

        index = i%N
        iterations = perfect_loops
        if index < rem:
            iterations+=1
        a= sequence[index]
        b =sequence[N-(index)-1]
        c = a^b
        selected_value = 1 + (iterations % 3)
            
    
        if index < half_loop:
            if selected_value == 1:
                new_sequence[index] = a
           

            elif selected_value == 2:
            
                new_sequence[index] = c
            
            elif selected_value == 3:
                new_sequence[index] = b
        
        else:
            if selected_value == 1:
                new_sequence[index] = a
           

            elif selected_value == 2:
            
                new_sequence[index] = b
            
            elif selected_value == 3:
                new_sequence[index] = c

 
        if index == N-(index)-1:
            new_sequence[index] = 0
            
        

    ans = True
    for i in range(N):
        if new_sequence[i] != new_sequence_2[i]:
            ans = False
            break
        # print(new_sequence[i],new_sequence_2[i])

    print(ans)








