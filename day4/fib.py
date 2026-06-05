n=int(input("enter the number of terms you want :"))
n1=0 # first term of fibonacii series
n2=1 # second term of  Fibonacci series
print("fibonacci series is:")
print(n1) 
print(n2)
for i in range(2,n):
    n3=n1+n2 # it is for the next term of fibonacci series so to find the next term we have to add the previous terms
    print(n3) # here we print the next term 
    n1=n2
    n2=n3