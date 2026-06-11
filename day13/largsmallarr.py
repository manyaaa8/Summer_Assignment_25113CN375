from array import *
vals=array("i",[])
n=int(input("enter the number of elements you want to insert:-"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    vals.append(x)
print("elements before sort:")
for elements in vals:
    print(elements,end=" ")
print()
print("Elements after sort:-")
v=sorted(vals)
for i in v:
    print(i,end=" ")
print()
print("the largest element is:-",v[0])
print("the smallest element is:-",v[-1])