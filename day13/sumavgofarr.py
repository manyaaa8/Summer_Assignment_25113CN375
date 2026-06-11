from array import *
sum=0
vals=array("i",[])
n=int(input("enter the number of elements you want to insert:-"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    vals.append(x)
    sum=sum+x
avg=sum/n
print("The sum of elements:-",sum)
print("The average of elements:-",avg)
    
    
