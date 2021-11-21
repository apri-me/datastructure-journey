'''
    Implementation of Bucket sort and an improved version for arbitrary elements.
'''
import math
def bucket_sort(array):
    answer = []
    counter = [[] for i in range(len(array))]
    for i in range(len(array)):
        counter[math.floor(len(array) * array[i])].append(array[i])
    for i in range(len(counter)):
        k = counter[i]
        k.sort()
        counter[i] = k
    for i in counter:
        for j in i:
            answer.append(j)
    return answer

def improved_bucket_sort(array):
    max_element = max(array)
    min_element = min(array)
    dictionary = {}
    for i in array:
        k = (i-min_element)/(max_element - min_element + 0.00001)
        dictionary[k] = i
    keys = dictionary.keys()
    keys = [float(i) for i in keys]
    keys = bucket_sort(keys)
    answer = []
    for i in keys:
        answer.append(dictionary[i])
    return answer