import doctest

#binary search
def binary_search(list, target):
    """Simple Binary Search
    >>> numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
    >>> target = 5
    >>> print(binary_search(numbers, target))
    0
    """
    max = len(list)
    min = 0
    
    while min <= max:
        mid = (min + max) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            min = mid + 1
        else:
            max = mid - 1
    return -1

from arrays import LinearArray
# for example
filename = 'file0.txt'
print('Processing', filename, 'with a linear array')
test_array = LinearArray()  # initialise a LinearArray
process_file(filename, test_array)

