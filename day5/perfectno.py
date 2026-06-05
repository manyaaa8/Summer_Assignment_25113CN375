# here we have to check whether it is perfect or not 
n=int(input("enter the number:"))
sum=0
for i in range (1,n): # in this range is use because we have to find the factors of the number
    if n%i==0:
        sum=sum+i # here we have to add each factor in sum variable 
if sum==n: # now we have to compare the sum with the given number if it is equal or not.
    print("it is a perfect number")
else:
    print("it is not a perfect number")