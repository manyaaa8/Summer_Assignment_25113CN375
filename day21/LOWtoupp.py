st=input("enter the string:-")
#print(st.upper()) this is with inbuilt  fn.In this time complexity is O(n)
newst=""
for i in st:
    if i>="a" and i<="z":
        a=ord(i)-32
        newst+=chr(a)
    else:
         newst+=i
       
print(newst)