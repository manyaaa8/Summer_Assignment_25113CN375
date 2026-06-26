from array import*
arr1=array("i",[])
arr2=array("i",[])
merge=array("i",[])
n=int(input("enter the number of elements you want:-"))
print("first array:-")
for i in range(0,n):
    x=int(input("enter the element:-"))
    arr1.append(x)
print("second array:-")
for i in range(0,n):
    ele=int(input("enter the element:-"))
    arr2.append(ele)
i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        merge.append(arr1[i])
        i += 1
    else:
        merge.append(arr2[j])
        j += 1
while i < len(arr1):
    merge.append(arr1[i])
    i += 1
while j < len(arr2):
    merge.append(arr2[j])
    j += 1
print("Merged Array:", merge)
