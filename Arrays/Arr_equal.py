from collections import Counter
def equal_arr(arr1,arr2):
    count_a1=Counter(arr1)
    count_a2=Counter(arr2)

    if count_a1 == count_a2:
        return 'true'
    return 'false'
arr1=[0,4,3,2,1]
arr2=[1,2,3,4,0]
print(equal_arr(arr1,arr2))
