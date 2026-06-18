from array import *
vals=array("i",[])
n=int(input("enter the number of elements you want to insert:-"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    vals.append(x)
# bubble sort   
for i in range(n-1):
    for j in range(n-1-i):
        if vals[j] >vals[j+1]:
            temp = vals[j]
            vals[j] = vals[j+1]
            vals[j+1] = temp
#binary search
print()
x=int(input("enter the number to br searched:"))
low=0
high=n-1
flag=0
while low<=high:
    mid=(low+high)//2
    if vals[mid]==x:
        flag=1
        break
    elif vals[mid]<x:
        low=mid+1
    elif vals[mid]>x:
        high=mid-1
if flag==1:
        print("Number",x,"is found at position",mid)
else:
    print("Nxumber",x,"is not found")