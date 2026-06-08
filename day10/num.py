rows=int(input("enter the number of rows:"))
for i in range(0,rows):
     for j in range(1,rows-i):
         print(" ",end="")
     for j in range (1,i+2):
          print(j,end="") 
     for j in range (1,i+1):
         print(i-j+1,end="")
     print()
     