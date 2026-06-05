def rev(n,d=0):
    if n==0:
        return d
    else:
        return rev(n//10,d*10+n%10)
n=int(input("enter the number:"))
print("the reverse of digit is:",rev(n))