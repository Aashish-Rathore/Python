def missing_num(arr,n):
    total= n*(n+1)//2
    return total - sum(arr)
arr=[1,2,4,5]
n=5
print(missing_num(arr,n))