from sys import stdin
t = int(stdin.readline())


def Rev(number):
    rev = 0
    n = number
    while(n > 0): 
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10
        
        
    return rev



for _ in range(t):
    mod = 10**9 + 7
    N,K = map(int,stdin.readline().strip().split(" "))
    sequence_A = []
    sequence_B = []
    sequence_C= []
    ran = (10**N)%mod
    for i in range(ran):
        sequence_A.append(i)
    print("Done")
    # c = 0
    # # sequence_B.append(0)
    # B_dict = {}
    # while c < len(sequence_A):
    #     if len(sequence_A) < K:
    #         break
    #     sequence_B.append(c)
    #     if c not in B_dict:
    #         B_dict[c] = True
    #     c+=K
        

    # for i in sequence_B:
        
    #     if i in B_dict and Rev(i) in B_dict:
            
    #         sequence_C.append(i)

    # print(len(sequence_C)%mod)





    

    
    
    