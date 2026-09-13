def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)


arr = [190, -44, -33, 12, 150, 16, 17, 20]
quickSort(arr, 0, len(arr) - 1)
print(arr)

# Time Complexity: Best Case: O(n log n), Average Case: O(n log n), Worst Case: O(n^2)

# Space Complexity: O(log n) 