def compress(arr):

    if len(arr) == 0:
        return 0

    current_element = arr[0]
    result_string = ""
    current_count = 1

    for alph in range(1, len(arr)):

        if arr[alph] == current_element:
            current_count += 1
            if alph == len(arr)-1:
                print(current_count)
                result_string += current_element+str(current_count)

        else:

            result_string += current_element+str(current_count)
            current_element = arr[alph]
            current_count = 1
            if alph == len(arr)-1:
                print(current_count)
                result_string += current_element+str(current_count)

    print(result_string)


compress("AAABCCDDDDDCCBBabcdaabbccdd")
