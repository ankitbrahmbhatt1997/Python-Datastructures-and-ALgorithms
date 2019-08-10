# from sys import stdin



# array,targetSum = list(map(int, stdin.readline().strip().split(" "))),int(input())

# print(array,targetSum)

# print("ok")


def twoNumberSum(array, targetSum):
    if len(array) < 2:
        return False

    seen = set()
    result = []

    for num in array:
        target = targetSum-num
        if target in seen:
            result = [num,target]
            break
        else:
            seen.add(num)

    result.sort()
    return result

print(twoNumberSum([4,6],10))



