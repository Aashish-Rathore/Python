def sec_lar(arr):
    first=second=float("-inf")
    for num in arr:
        if num > first:
         second = first 
         first = num
        elif num > second and num!=first :
           second = num
    return second if second!=float("-inf") else None
arr=[10,8,5,3,2,1]
print(sec_lar(arr))