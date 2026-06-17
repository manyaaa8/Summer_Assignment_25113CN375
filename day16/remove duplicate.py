from array import *
arr = array("i",[])
n = int(input("enter the number of elements to be inserted:-"))
for i in range(n):
    x = int(input("ENTER THE ELEMENTS:-"))
    arr.append(x)
newarr = array("i",[])
for i in arr:
    if i not in newarr: #use membership operator to check whether i is not present in newarr if not then 
        newarr.append(i) #append the element
arr=newarr
print(arr)