def add_num(x,y):
    return x+y

res = add_num(3,4)
print(res)



i = 1
while i<=5:
    print(i)
    i+=1



fruits = ["apple","banana","pinepaple","mango","kiwi"]
for fruit in fruits:
    print(fruit)



list = [10,20,30,40,50]
print(list[0])
print(list[-1])
print(list[1:3])
print(list[::-1])




grades = {"aman":54, "samay":89 , "vohem":99}
print("aman's grade=",grades["aman"])

grades["David"]=88
print(grades)

for guys,grade in grades.items():
    print(guys,"have the grades",grade)





squares=[]
for x in range(1,6):
    squares.append(x**2)
print(squares)




sqr_compresion=[x**2 for x in range(1,6)]
print(sqr_compresion)



add_lamda =lambda a,b : a+b
res=add_lamda(3,4)
print(res)





# //MAP-->
n=[1,2,3,4,5]

sqr_nub= list(map(lambda x: x**2 ,n))
print(sqr_nub)

# FILTER-->
even_nub=list(filter(lambda x: x%2==0,n))
print(even_nub)

# REDUCE-->
from functools import reduce
sum_of_num=reduce(lambda x,y: x+y,n)
print(sum_of_num)


class Car:
    def __init__(self,color,engine,price):
        self.color= color
        self.engine = engine
        self.price = price

    def drive(self):
        print(f"{self.engine} runs very smoothly" )

my_car = Car("crimson red","v8 turbo engine","above 1cr")




def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr=[2,9,1,0,3,7,3,2,76,1]
bubble_sort(arr)
print(arr)



def linear_search(arr,X):
    for i in range(len(arr)):
        if arr[i]==X:
            return i      
    return -1

arr=[2,1,4,5,6,8,9]
print(linear_search(arr,5))




def binary_search(arr, X):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = (start+end) // 2
        if arr[mid]==X:
            return mid
        elif arr[mid]<X :
           start= mid+1
        else:
           end = mid-1
    return -1

arr=[1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr,7))




def left_rotate(arr,d):
    n=len(arr)
    arr[:] = arr[d:n] + arr[0:d]
    return arr

arr=[1,2,3,4,5]
print(left_rotate(arr,2))



# 1 largestinArray-->
def lar_arr(arr):
    large = arr[0]
    for num in arr:
       if num > large:
        large = num
    return large
arr=[9,7,88,65,4,4,1]
print(lar_arr(arr))



# 2 smallest
def small_arr(arr):
    smallest= arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
arr=[12,1,2,3,6]
print(small_arr(arr))



# 3 totalSum-->
def sum(arr):
    total = 0
    for i in arr:
        total+=i
    return total
arr=[12,13,14,15,16]
print(sum(arr))



# 4 REVERSE ARRAY-->
def rev_arr(arr):
    s,e= 0,len(arr)-1
    while s < e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    return arr
#         return arr[::-1]
arr=[10,9,8,7,6,5]
print(rev_arr(arr))


# 5 SEcond largest in array-->
def sec_lar(arr):
   first = second = float('-inf')
   for num in arr:
      if  num > first:
         second=first
         first = num
      elif num > second and num!=first:
         second=num
         return second if second!=float('-inf') else None
     
arr=[10,8,5,3,2,1]
print(sec_lar(arr))



# 6 sorted array-->
def is_sorted(arr):
    for num in range(len(arr)-1):
        if arr[num]>arr[num+1]:
            return False
        return True
arr=[1,2,3,5,6]
print(is_sorted(arr))



# 7 Remove Duplicates-->
def duplicate(arr):
    unique_element= []
    for i in arr:
        if i not in unique_element:
            unique_element.append(i)
    return unique_element
arr=[10,3,4,5,6,7,10,3,7]
print(duplicate(arr))




# 8 count Frequency-->
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