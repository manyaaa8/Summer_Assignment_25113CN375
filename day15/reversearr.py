from array import * 
arr=array("i",[])
n=int(input("enter the number of elements you want:-"))
for i in range (0,n):
    x=int(input("ENTER THE ELEMENT:-"))
    arr.append(x)
print("ARRAY BEFORE REVERSING:-")
for ar in arr:
 print (ar,end=" ")
print()
print("ARRAY AFTER REVERSING")
for i in range(n-1,0,-1):
    print(arr[i],end=" ")