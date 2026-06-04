n=int(input("enter the number:"))
rev=0
num=n
while(n !=0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(num==rev):
    print("the number",num,"is palindrome")
else:
    print("the number",num,"is not palindrome")