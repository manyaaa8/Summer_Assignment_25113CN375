def perfect(n,sum=0):
    for i in range(1,n):
        if n%i==0:
          sum=sum+i
    return sum
n=int(input("enter the number:-"))
temp=perfect(n)
if temp==n:
    print("it is a perfect number")
else:
    print("it is not a perfect number")