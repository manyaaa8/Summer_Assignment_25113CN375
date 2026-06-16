from array import *
arr=array("i",[])
n=int(input("enter the number of elements to be inserted:-"))
for i in range(n):
    x=int(input("ENTER THE ELEMENTS:-"))
    arr.append(x)
new=set(arr)
for i in new:
 print(i,end=" ")