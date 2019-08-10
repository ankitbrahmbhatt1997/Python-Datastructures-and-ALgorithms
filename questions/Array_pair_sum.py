import time

start_time = time.time()


def array_pair_sum(arr, k):
    if len(arr) < 2:
        return False

    seen = set()
    result = set()

    for num in arr:
        target = k-num
        if target in seen:
            result.add((num, target))
            break
        else:
            seen.add(num)

    return result


print(array_pair_sum([1, 2, 3, 2], 4))
print("Time Taken is {}".format(time.time()-start_time))
