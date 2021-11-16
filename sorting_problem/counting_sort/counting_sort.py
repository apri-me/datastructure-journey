#Implementing counting sort algorithm with assumption that min(A) = 0 and max(A) = k
def counting_sort(A, k):
    answer = [None for _ in range(len(A))]
    C = [0 for _ in range(k+1)]
    for i in range(len(A)):
        C[A[i]] += 1   
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for i in range(len(A)-1, -1, -1):
        answer[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return answer