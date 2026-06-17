from array import *
arr1=array("i",[55,43,67,56,89])
arr2=array("i",[4,56,7,9,9,8])
union_array=array("i",[])
for i in arr1:
    if i not in union_array:
     union_array.append(i)
for j in arr2:
    if j not in union_array:
        union_array.append(j)        
print(union_array)