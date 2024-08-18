n = 5

for i in range(1,n+1):
    print()
    for j in range(5,n+i):
        print(" ",end=" ")
    for z in range(2*i-5,6):
         print("*",end=" ")
print()