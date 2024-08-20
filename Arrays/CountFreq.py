def count_freq(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num]=1
    return frequency

arr=[1,2,3,4,5,1,2,3,3,3,3,4,4,4,2,3]
print(count_freq(arr))