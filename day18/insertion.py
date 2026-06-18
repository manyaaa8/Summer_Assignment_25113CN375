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
    key=i
    for j in range(i+1,n):
        if vals[key] >vals[j]:
            key=j
    temp = vals[i]
    vals[i] = vals[key]
    vals[key] = temp
print()
print("AFTER SORTINGG:-")
for j in vals:
 print(j,end=" ")