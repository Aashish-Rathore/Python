def search_arr(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i+1
    return-1
arr=[1,3,4,16,7,66,42]
k=16
print(search_arr(arr,k))
