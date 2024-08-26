def peak_element(arr,n):
    for i in range(n):
        if(i==0 or arr[i]>arr[i-1]) and (i==n-1 or arr[i]>arr[i+1]):
            return 1
    return 0
arr=[5,6,7]
n=3
print(peak_element(arr,n))
