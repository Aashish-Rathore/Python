def unique_element(input_list):
    uniq_elem=[]
    for elem in input_list:
        if elem not in uniq_elem:
            uniq_elem.append(elem)
    return uniq_elem
input_list=[1,2,3,4,1,2,4,3]
print(unique_element(input_list))