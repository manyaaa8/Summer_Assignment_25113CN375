def sum(n):
    if n==0:
        return 0
    else:
        return n%10+sum(n//10)
n=int(input("enter the number:"))
print("the sum of digits is:",sum(n))