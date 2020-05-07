def GCD(a,b):
    if a % b == 0:
        return b
    else:
        return GCD(b,a%b)

def solution(N, M):
    gcd = GCD(N,M)
    if gcd == 0:
        return N
    return N//gcd
    

print(solution(11,11))
