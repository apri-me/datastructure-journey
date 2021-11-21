def counting_sort(A, b, k, indices):
    n = len(indices)
    answer = [None] * n
    C = [0] * (k+1)
    for i in indices:
        C[ord(A[i][b])] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for i in range(n-1, -1, -1):
        ind = ord(A[indices[i]][b])
        answer[C[ind] - 1] = A[indices[i]]
        C[ind] -= 1
    for i, j in enumerate(indices):
        A[j] = answer[i]


# This implementation of radix sort is time optimized for strings with different lenghts.
def radix_sort(arr):
    arr_max = max(arr)
    max_digit = len(arr_max) - 1

    for b in range(max_digit, -1, -1):
        indices = [i for i in range(len(arr)) if b + 1 <= len(arr[i])]
        counting_sort(arr, b, 255, indices)
