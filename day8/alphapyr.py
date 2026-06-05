rows=int(input("enter the number of rows:"))
for i in range(0,rows):
    for j in range(65,65+i+1):
        print(chr(j),end="")
    print()