from array import *
arr=array("i",[8,6,7,5,4,2,1])
size=len(arr) # getting the length of array for usonh it in loop
s=set(arr) # in this we use set because it give us (O)n time complexity which is better 
for i in range(1,size+1):
  if i not in s: # if the( element ) is not present in  set then ADD it
      print(i)
    
    