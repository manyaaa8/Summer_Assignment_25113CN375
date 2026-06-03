n=int(input("enter the number"))
fac=1
if (n<0):
    print("there is noo factorial for negative numbers")
elif (n==0):
    print("factorial is 1")
else :
    for i in range(1,n+1):
        fac=fac*i
    print("the factorial of",n,"is :",fac)    