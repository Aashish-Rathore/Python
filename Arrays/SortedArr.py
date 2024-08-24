def is_sorted(arr):
    for num in arr:
        if arr[num]>arr[num+1]:
            return False
        return True
    return num
arr=[1,2,3,5,6]
print(is_sorted(arr))
