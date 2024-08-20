def duplicate(arr):
    unique_element= []
    for i in arr:
        if i not in unique_element:
            unique_element.append(i)
    return unique_element
arr=[10,3,4,5,6,7,10,3,7]
print(duplicate(arr))
