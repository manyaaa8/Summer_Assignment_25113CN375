def armstrong(n,dig=0):
    while n>0:
        d=n%10
        dig=dig+d*d*d
        n=n//10
    return dig
n=int(input("enter the 3-digit number to be checked:-"))
num=n
temp=armstrong(n)
if num==temp:
    print("number is armstrong")
else:
    print("number is not armstrong")