rows=int(input("enter the number of rows:"))
for i in range(rows+1,1,-1):
    for j in range(1,i):
        print("*",end="")
    print()