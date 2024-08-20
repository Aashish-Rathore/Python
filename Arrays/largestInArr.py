def lar_arr(arr):
    large = arr[0]
    for num in arr:
       if num > large:
        large = num
    return large
arr=[9,7,88,65,4,4,1]
print(lar_arr(arr))