name_list=[]
n=int(input("enter the number of name you want to insert:- "))
for i in range(n):
    st=input("ENTER THE NAME:-")
    name_list.append(st)
sec=sorted(name_list)
print(sec)