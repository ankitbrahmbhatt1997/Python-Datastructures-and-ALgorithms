def longest_substring(k, arr):
    if len(arr) == 0:
        return 0

    longest_substring = arr[0]

    for i in range(0, len(arr)-1):
        current_element = arr[i]
        current_substring = arr[i]
        distinct_elements = [arr[i]]
        j = i
        while len(distinct_elements) <= 2 and j < len(arr):

            if len(distinct_elements) < 2 and arr[j+1] != current_element:
                current_substring += arr[j+1]
                current_element = arr[j+1]
                distinct_elements.append(arr[j+1])
                print(current_substring)
                j += 1
            elif arr[j+1] and arr[j+1] in distinct_elements:
                current_substring += arr[j+1]
                current_element = arr[j+1]
                j += 1
            else:
                break
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    return longest_substring


print(longest_substring(2, "abcba"))
