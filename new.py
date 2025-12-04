def median_of_three_partition(a):
    low, high = 0, len(a) - 1
    mid = (low + high) // 2

    # Step 1: find median of first, middle, last
    trio = [(a[low], low), (a[mid], mid), (a[high], high)]
    trio.sort(key=lambda x: x[0])
    pivot_value, pivot_index = trio[1]

    # Step 2: move pivot to end (common convention)
    a[pivot_index], a[high] = a[high], a[pivot_index]

    # Step 3: partition using Lomuto scheme
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
            print(a)
    a[i + 1], a[high] = a[high], a[i + 1]


    return i + 1  # final pivot position

arr = [12, 48, 15, 8, 85, 2, 3, 1, 72, 26, 4]
pivot_pos = median_of_three_partition(arr)
print("After partition:", arr)
print("Pivot index:", pivot_pos)
