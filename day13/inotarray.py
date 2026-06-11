from array import *
vals=array("i",[])
n=int(input("enter the number of elements you want to insert:-"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    vals.append(x)
for elements in vals:
    print(elements,end=" ")
