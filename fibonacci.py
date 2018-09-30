# using recursion
def fibonacci_with_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_with_recursion(n-1) + fibonacci_with_recursion(n-2)


dic = {}


def fibonacci_with_recursion_and_memoization(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n in dic:
            return dic[n]
        else:
            dic[n] = fibonacci_with_recursion_and_memoization(
                n-1) + fibonacci_with_recursion_and_memoization(n-2)
            return dic[n]


print(fibonacci_with_recursion(6))
print(fibonacci_with_recursion_and_memoization(6))
