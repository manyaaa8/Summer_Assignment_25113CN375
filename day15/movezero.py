from array import * 
arr=array("i",[])
n=int(input("enter the number of elements you want:-"))
for i in range (0,n):
    x=int(input("ENTER THE ELEMENT:-"))
    arr.append(x)
print("THE ARRAYY IS:-")
for ar in arr:
 print (ar,end=" ")
print()
print("AFTER MOVING ZERO TO END IT IS:-")
count=0
i=0
while i < len(arr):
    if arr[i] == 0:
        arr.pop(i)
        count += 1
    else:
        i += 1

for zeroes in range(0,count):
    arr.append(0)
print(arr)
        