def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Out of the while loop!

numbers = [12, 11, 13, 5, 6]
insertion_sort(numbers)
print("Sorted:", numbers)

# Time:  Best: O(n), Avg: O(n^2), Worst: O(n^2)
# Space: O(1)