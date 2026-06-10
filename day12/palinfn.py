def palin(n,rev=0):
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev
n=int(input("enter the number to be checked:-"))
num=n
temp=palin(n)
if num==temp:
    print("number is palindrome")
else:
    print("number is not palindrome")
