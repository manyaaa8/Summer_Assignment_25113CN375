st=input("enter the string:-")
#print(st[::-1]) this is with inbuilt  fn.In this time complexity is O(n)
newst=""
j=len(st)-1
while j>=0:
    newst+=st[j]
    j-=1
print(newst) # in this time complexity is O(n^2)
    
    
    