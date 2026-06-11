from array import *
vals=array("i",[])
odd=even=0
n=int(input("enter the number of elements you want to insert:-"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    vals.append(x)
    if i%2==0:
        even+=1
    else:
        odd+=1
for elements in vals:
    print(elements,end=" ")
print()
print("TOTAL NUMBER OF ODD ELEMENT IS:-",odd)
print("TOTAL NUMBER OF EVEN ELEMENT IS:-",even)
