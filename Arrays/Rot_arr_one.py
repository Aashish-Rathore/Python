def rotate_arr(arr):
    last_elem=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last_elem
    return arr
arr=[1,2,3,4,5]
print(rotate_arr(arr))