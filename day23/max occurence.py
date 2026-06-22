st=input("ENTER THE STRING :-")
dic={}
for i in st:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
max_char=max(dic.values())
for key,value in dic.items():
   if value==max_char:
       print("the most occuring charvater is",key,"with",value,"no. of times")
    