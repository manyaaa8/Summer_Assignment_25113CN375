st=input("ENTER THE STRING :-")
char_set=set()
for i in st:
    if i in char_set:
        print("the first repeating character is",i)
        break
    else:
         char_set.add(i)
else:
   print("no repeating character present")
        
    