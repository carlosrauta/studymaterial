def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin <= end:
        mid = (begin + end) // 2
        if array[mid] == item:
            return mid
        elif item < array[mid]:
            return binary_search(array, item, begin, mid - 1)
        else:
            return binary_search(array, item, mid + 1, end)
    return None


# test case
array = [2, 3, 4, 10, 40]
print(f'It is located in index {binary_search(array, 3)}')
