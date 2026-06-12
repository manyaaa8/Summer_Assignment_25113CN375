from array import *
vals=array("i",[])
flag=0 #initialising  the value
n=int(input("enter the number of elements you want to insert:-"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    vals.append(x) #method to insert the elements in array
x=int(input("enter the number to be searched:-"))
for num in vals:#using loop for search
    if num==x: # if the element is present in array then
        flag=1 #the flag value changes to 1
        break #terminating the loop
if flag==1: #comparing the value of flag to know whether the elent is present or not
    print("The element is present")
else:
    print("The number is not present")