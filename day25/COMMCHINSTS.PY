st1=input("ENTER THE FIRST STRING :- ")
st2=input("ENTER THE SECOND STRING :- ")
d1={}
d2={}
for i in st1:
        d1[i]=d1.get(i,0)+1
for j in st2:
        d2[j]=d2.get(j,0)+1
for ch in d1:
    if ch in d2:
     a=min(d1[ch],d2[ch])
     for i in range(a):
        print(ch,end="")     
        
