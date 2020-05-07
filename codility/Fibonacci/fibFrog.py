def fibonacci(N):
    fib = [0]*(N+1)
    fib[1] = 1
    for i in range(2,N+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

def solution(A):
    fib = fibonacci(len(A))

    return fib


print(solution([0,0,0,1,1,0,1,0,0,0,0]))

