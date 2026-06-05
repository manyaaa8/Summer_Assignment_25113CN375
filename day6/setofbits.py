n=int(input("enter the number:"))
bits=0
while(n>0):
    d=n%2
    if d==1:
        bits+=1
    n=n//2
print("the number of bits is:",bits)