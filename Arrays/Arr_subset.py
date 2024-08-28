from collections import Counter
def array_subset(a1,a2):
    count_a1=Counter(a1)
    count_a2=Counter(a2)

    for elem in a2:
        if count_a2[elem] > count_a1.get(elem,0):
            return 'No'
    return 'Yes'
a1=[1,2,3,4,4,5,6]
a2=[1,2,4]
print(array_subset(a1,a2))