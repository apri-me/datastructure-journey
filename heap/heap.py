# Implementation of heap functions

import math

def left(i):
    return 2*i

def right(i):
    return i * 2 + 1

def parent(i):
    return i // 2

def max_heapify(array, i):
    largest = i
    l = left(i)
    r = right(i)
    if l <= len(array) - 1 and array[l] > array[i]:
        largest = l
    if r <= len(array) - 1 and array[r] > array[largest]:
        largest = r
    if largest != i:
        array[i] , array[largest] = array[largest], array[i]
        max_heapify(array, largest)

def build_max_heap(array):
    for i in range(math.floor((len(array)-1)/2), 0, -1):
        max_heapify(array, i)

def heap_sort(array):
    build_max_heap(array)
    heap_size = len(array) - 1
    for i in range(heap_size, 0, -1):
        array[i], array[1] = array[1], array[i]
        max_heapify(array, i)

#Just consider index your array from 1 to n and using a list with n + 1 elements! First element is not useful at all.