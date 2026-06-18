from array import *
vals=array("i",[])
n=int(input("enter the number of elements you want to insert:-"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    vals.append(x)
print("BEFORE SORTING :-")   
for ele in vals:
    print(ele,end=" ") 
for i in range(n-1):
    for j in range(n-1-i):
        if vals[j] <vals[j+1]:
            temp = vals[j]
            vals[j] = vals[j+1]
            vals[j+1] = temp
print()
print("AFTER SORTINGG:-")
for j in vals:
 print(j,end=" ")