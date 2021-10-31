from math import floor


def merge(A, p, q, r):
    R = A[p: q+1]
    n1 = len(R) - 1
    i = 0
    j = q + 1
    s = p
    while i <= n1 and j <= r:
        if R[i] <= A[j]:
            A[s] = R[i]
            i += 1
        else:
            A[s] = A[j]
            j += 1
        s += 1
    if i <= n1:
        for t in range(s, r+1):
            A[t] = R[i]
            i += 1


def merge_sort(A, p=0, r=None):
    if r is None:
        r = len(A) - 1
    if p < r:
        q = floor((p+r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

