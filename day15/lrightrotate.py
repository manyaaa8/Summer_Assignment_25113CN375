from array import *
arr=array("i",[])
n=int(input("enter the number of elements you want to insert:"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    arr.append(x)
space=int(input("THE NUMBER OF SPACES TO SHIFT TO RIGHT SIDE OR ROTATE TO RIGHT:-"))
print("BEFORE ROTATION ELEMENTS ARE:-")
for ar in arr:
    print(ar,end=" ")
print()
space=space%n
arr= arr[-space:] + arr[:-space]
print("AFTER ROTATION:-")
for j in arr:  
    print(j,end=" ")