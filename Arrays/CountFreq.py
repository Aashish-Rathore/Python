def count_freq(arr):
  freq ={}
  for num in arr:
    if num in freq:
       freq[num]+=1
    else:
       freq[num]=1
  return freq
      
arr=[1,2,3,4,5,1,2,3,3,3,3,4,4,4,2,3]
print(count_freq(arr))

