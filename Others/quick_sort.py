from sys import stdin


def partition(arr, low, high):
    i = low-1
    j = low

    while j < high:
        if arr[j] <= arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        j += 1

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i


def quick_sort(arr, low, high):

    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)


t = int(stdin.readline())
arr = []
for i in range(t):
    arr.append(int(stdin.readline()))

arr.sort()
for i in arr:
    print(i)
