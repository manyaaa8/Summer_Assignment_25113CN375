n=int(input ("enter a 3-digit number :"))
arm=0
temp=n
while(n!=0):
    d=n%10
    arm=arm+(d*d*d) # here we have to find the cube of each digit and add it in arm variable because we have to compare it with the given number.
    n=n//10
if (temp==arm):
    print("it is an armstron number")
else:
    print("it is not a armstrong number")