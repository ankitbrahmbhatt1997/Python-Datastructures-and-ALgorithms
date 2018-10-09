def partition(A, p, r):
    q = j = p
    while j < r:
        if A[j] <= A[r]:
            A[q], A[j] = A[j], A[q]
            q += 1
        j += 1
    A[q], A[r] = A[r], A[q]
    return q


def quicksort(A, p, r):
    if r > p:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


arr = [10, 2, 4, 7, 5, 9, 3]
quicksort(arr, 0, len(arr)-1)
print(arr)
