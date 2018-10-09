from sys import stdin


def oppositeSigns(x, y):
    return ((x ^ y) < 0)


def alt_subarray(arr, index):
    if index == len(arr):
        return 0
    elif index == len(arr)-1:
        return 1
    else:
        if index in dic:
            return dic[index]
        else:
            if not oppositeSigns(arr[index], arr[index+1]):
                dic[index] = 1
                return dic[index]
            else:
                dic[index] = 1+alt_subarray(arr, index+1)
                return dic[index]


t = int(stdin.readline())

for i in range(t):
    dic = {}
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))

    for j in range(0, len(arr)):
        print(alt_subarray(arr, j), end=" ")

    print("")
