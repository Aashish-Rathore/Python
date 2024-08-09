arr = [1,2,4,5,50]
print(arr)


# Array implementation -->
# print("how many element to store inside the array",end=" ")
# num=input()
# arr=[]
# print("\nEnter",num,"Element: ",end="")
# num=int(num)
# for i in range (num):
#     element = input()
#     arr.append(element)
# print("\nThe array element are")
# for i in range(num):33
#     print(arr[i],end=" ")


# 2D Array -->
r_num = int(input("enter the no of rows"))
c_num = int(input("enter the no of cols"))
twod_arr = [[0 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        twod_arr[row][col]=row*col
print(twod_arr)