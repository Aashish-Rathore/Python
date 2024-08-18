n = 5  

for i in range(n):
    char = 65 + n - i - 1  
    for j in range(n - i):
        print(chr(char), end=" ")
        char -= 1  
    print()
