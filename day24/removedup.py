st=input("ENTER THE STRING:- ")
newst=""
for i in st:
    if i not in newst:
        newst+=i
print("the new string is:-", newst)