def imm_smal_ele(arr,n):
    for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i]=arr[i+1]
            else:
                arr[i]=-1
    arr[n-1]=-1
    return arr

arr=[4,2,1,5,3]
print(imm_smal_ele(arr,5))