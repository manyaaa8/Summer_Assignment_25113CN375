st=input("ENTER THE STRING:-")
newst=""
count=1
for i in range(1,len(st)):
    if st[i]==st[i-1]:
        count+=1
    else:
        newst+=st[i-1]+str(count)
        count=1
newst+=st[-1]+str(count)
print(newst)
