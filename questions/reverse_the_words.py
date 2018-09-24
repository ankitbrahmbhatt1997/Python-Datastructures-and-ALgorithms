def reverse_the_string(arr):

    if len(arr) == 0:
        return 0

    arr = arr.strip()

    str_arr = arr.split(" ")
    rev_arr = []
    for i in range(len(str_arr)-1, -1, -1):
        rev_arr.append(str_arr[i])

    return rev_arr


print(reverse_the_string("Does God Exist    "))
