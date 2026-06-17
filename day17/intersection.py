from array import *
arr1=array("i",[55,43,67,56,89])
arr2=array("i",[4,56,7,9,9,8])
intersection=array("i",[])
for i in arr1:
  for j in arr2:
    if (i==j) and (j not in intersection):
     intersection.append(j)        
print (intersection)