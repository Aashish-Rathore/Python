def arr_eq_ind(arr):
    result=[]
    for i in range(len(arr)):
        if arr[i] ==i+1:
            result.append(i+1)
    return result
arr=[1,2,345,4,65] 
print(arr_eq_ind(arr))