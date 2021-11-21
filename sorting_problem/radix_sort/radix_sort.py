
def find_digit(num, exp, b):
    return (num // exp) % b


def counting_sort(A, exp, k):
    n = len(A)
    answer = [None] * n
    C = [0] * (k+1)
    for i in range(n):
        C[find_digit(A[i], exp, k+1)] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for i in range(n-1, -1, -1):
        ind = find_digit(A[i], exp, k+1)
        answer[C[ind] - 1] = A[i]
        C[ind] -= 1
    for i in range(n):
        A[i] = answer[i]


def radix_sort(arr):
    arr_max = max(arr)
    exp = 1
    while 0 < exp < arr_max:
        counting_sort(arr, exp, 9)
        exp *= 10