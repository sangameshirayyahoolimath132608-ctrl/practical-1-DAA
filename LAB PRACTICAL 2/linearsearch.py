def linearSerch(arr, target):
    n = len(arr)
    for i in range(0, n):
        if arr[i]==target:
            return i
    return -1

arr = [10,20,-4,90,2,22]
target = 22
ans = linearSerch(arr,target)
print(ans)

# Time Complexity, Best Case   : O(1), Average Case: O(n), Worst Case  : O(n)
# Space Complexity:   O(1)