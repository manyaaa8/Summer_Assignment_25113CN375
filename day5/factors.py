n=int(input("enter the number:"))
print("the factors of the number are:")
for i in range(1,n+1): 
    if n%i==0: # comdition to check whether it is a factor if it is then its remainder will be zero.
        print(i)