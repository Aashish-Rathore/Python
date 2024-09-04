def min_max(arr):
    arr.sort()
    return arr[0],arr[-1]

arr=[1,3456,43,334,22,3]
print(min_max(arr))