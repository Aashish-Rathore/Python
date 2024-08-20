def small_arr(arr):
    smallest= arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
arr=[12,1,2,3,6]
print(small_arr(arr))
