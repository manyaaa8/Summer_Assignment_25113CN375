def fib(n,term1=0,term2=1):
    print(term1 , term2,end=" ")
    for i in range(2,n):
        nextterm=term1+term2
        print(nextterm,end=" ")
        term1=term2
        term2=nextterm 
n=int(input("enter the number of terms you want:-"))
print("the fibnocii series is:")
fib(n)

