n=int(input("enter the binary number:"))
dec=0
p=0
import math
while n>0:
    d=n%10
    dec=dec+pow(2,p)*d
    p+=1
    n=n//10
print("the decimal number is:",dec)