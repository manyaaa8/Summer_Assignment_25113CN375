n=int(input("enter the number of terms you want :"))
n1=0 # first term of fibonacci series
n2=1 # second term of fibonacci series
for i in range(2,n): # here we have start the range from 2 as we have intiailized first 2 terms n1 and n2 
    n3=n1+n2 # it is for the next term of fibonacci series so to find the next term we have to add the previous terms
    n1,n2=n2,n3 
print("the nth term of fibonacci is:",n3)