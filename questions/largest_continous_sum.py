import time

start_time = time.time()


def largest_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum = cont_sum = start_number = arr[0]

    end_number = 0

    for num in arr[1:]:

        if cont_sum+num > num:
            cont_sum = cont_sum+num
        else:
            cont_sum = num
            start_number = num

        if cont_sum > max_sum:
            max_sum = cont_sum
            end_number = num

    return [max_sum, start_number, end_number]


print(largest_cont_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

print("Time Taken is {}".format(time.time()-start_time))
