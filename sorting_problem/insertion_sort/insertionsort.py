# Insertion Sort implementation:            D & D by : M.Nesari
def insertion_sort(arr):
    if len(arr) == 0:  # Check if arr is null!
        return
    else:
        print("Level 0 : ", arr)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j > -1 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j+1] = key
            print(f"Level {i} : ", arr)


length = int(input("Please enter your data length: "))
arr = []
inputs = input("Please enter your numbers with one space in between: ").split()
for i in inputs:
    arr.append(int(i))
insertion_sort(arr)
print("Sorted array : ", arr)
