def fac1(n,fac=1):
    if n<0:
     print("no factorial exist")
    elif n==0:
        return 1
    else:
      for i in range(1,n+1):
        fac=fac*i
      return fac
n=int(input("enter the number:"))
print("the factorial is",fac1(n))