import time

start_time = time.time()


def find_missing_element(arr1, arr2):

    count = {}

    for i in arr1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in arr2:
        if i in count:
            count[i] -= 1
        else:
            return i

    for i in count:
        if count[i] != 0:
            return i


print(find_missing_element([5, 5, 7, 7], [5, 5, 7]))

print("Time Taken is {}".format(time.time()-start_time))
