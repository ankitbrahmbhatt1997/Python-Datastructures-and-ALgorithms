from sys import stdin
t= int(stdin.readline())
for _ in range(t):
    N = int(stdin.readline())
    sequence = list(map(int,stdin.readline().strip().split(" ")))
    max_star_value = 0
    # for i in range(N):
    #     if i == 0:
    #         continue
    #     subSequence = sequence[:i]
    #     current_star_value = 0
    #     for j in subSequence:
    #         if j % sequence[i] == 0:
    #             current_star_value+=1
    #     if current_star_value > max_star_value:
    #         max_star_value = current_star_value
    count=0
    for i in range(N-1,-1,-1):
        if i == 0:
            continue
        count+=1
        current_star_value=0
        for j in range(i-1,-1,-1):
            if sequence[j] % sequence[i] == 0:
                current_star_value+=1
        if current_star_value > max_star_value:
            max_star_value = current_star_value
        if current_star_value == N-count-1:
            break




        
    print(max_star_value)

    