rows=int(input("enter the number of rows:"))
k=64
for i in range(0,rows):
     for j in range(1,rows-i):
         print(" ",end="")
     for j in range (1,i+2):
          print(chr(k+j),end="") 
     for j in range (1,i+1):
         print(chr(k+i-j+1),end="")
     print()