n=int(input("enter the number:"))
prod=1
while(n !=0):
    d=n%10
    prod=prod*d
    n=n//10
print("the product of the digit is",prod)