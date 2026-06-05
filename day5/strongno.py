n=int(input("enter the number:"))
sum=0
m=str(n) #here we use str to convert the number into string so that we can traverse in it.
for i in m:
    i=int(i) #here we have to covert the i into int as use cannot use range function with string.
    fac=1
    for j in range(1,i+1):
        fac=fac*j
    sum=sum+fac # each individual number factorial is added to the sum variable.
if sum==n: # for comparing if the sum is equal to the given number or not.
    print("it is a strong number")
else:
    print("it is not a strong number")