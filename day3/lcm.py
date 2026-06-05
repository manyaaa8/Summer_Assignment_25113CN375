num1=int(input("enter the first number:"))
num2=int(input("enter the second numbeer:"))
if num1<num2:
  for i in range(1,num1+1):
     if num1%i==0 and num2%i==0:
         gcd=i
else:
    for i in range(1,num2+1):
         if num1%i==0 and num2%i==0:
             gcd=i
lcm=(num1*num2)//gcd
print("the lcm of numbers is:",lcm)