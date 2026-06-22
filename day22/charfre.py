st=input("ENTER THE STRING:- ")
char_dic={}
for i in st:
    if i not in char_dic:
        char_dic[i]=1
    else:
        char_dic[i]+=1
for key,value in char_dic.items():
    print("the character:-", key ,"|| frequency:- ",value)