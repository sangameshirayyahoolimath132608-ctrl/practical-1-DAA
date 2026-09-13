def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print("Sorted:", numbers)

# Time:  Best: O(n^2), Avg: O(n^2), Worst: O(n^2)
# Space: O(1)