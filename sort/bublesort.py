#Bubble Sort implementation.
def bubbleSort(array):
    for i in range(len(array) - 1, -1, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array = exchange(array, j, j+1)
        print(array)
    return array

#Exchange function implementation.
def exchange(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array

#Improved bubble sort implementation.
def improvedBubbleSort(array):
    flag = True
    for i in range(len(array) - 1, -1, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array = exchange(array, j, j+1)
                flag = False
        print(array)
        if flag:
            break
    return array

a = input().split()
nums = []
for i in a:
    nums.append(int(i))
answer = bubbleSort(nums)
print(answer)