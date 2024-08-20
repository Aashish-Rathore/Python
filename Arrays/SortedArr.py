def is_sorted(arr):
    for num in range(len(arr)-1):
        if arr[num]>arr[num+1]:
            return False
        return True
arr=[1,2,3,5,6]
print(is_sorted(arr))

