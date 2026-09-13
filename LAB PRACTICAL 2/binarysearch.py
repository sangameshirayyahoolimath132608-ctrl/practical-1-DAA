def binarySearch(arr, key):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr=[1, 2 , 3, 4, 5, 6, 7]
key = 5
ans = binarySearch(arr, key)
print(ans)

# Time Complexity, Best Case   : O(1), Average Case: O(log n), Worst Case  : O(log n)
# Space Complexity:   O(1)