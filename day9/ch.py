rows=int(input("enter the number of rows:"))
k=64
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(k+i),end="")
    print()