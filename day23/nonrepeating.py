st=input("ENTER THE STRING :-")
dic={}
flag=0
for i in st:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    if dic[i]==1:
        print("the first non repeating character is",i)
        flag=1
        break
if flag !=1:
    print("noo non-repeating character found")