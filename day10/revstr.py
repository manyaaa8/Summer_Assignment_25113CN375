rows=int(input("enter the number of rows:"))
for i in range(rows+1,1,-1):
     for j in range(i-1,rows):
         print(" ",end="")
     for j in range (1,2*i-2):
         print("*",end="")    
     print()
     
 
    