def sort(array: list, i=None) -> None:
    """Sort array[:i+1]"""
    if i is None:
        i = len(array) - 1
    if i >= 1:
        j = prefix_max(array, i)
        array[i], array[j] = array[j], array[i]
        sort(array, i - 1)


def prefix_max(array: list, i: int) -> int:
    """Return index of maximum item in array[:i+1]"""
    if i >= 1:
        j = prefix_max(array, i-1)
        if array[i] < array[j]:
            return j
    return i
