n=int(input("enter the number:"))
print("the factors of the number are:")
a=[]
b=[]
for i in range(1,n+1): 
    if n%i==0: # comdition to check whether it is a factor if it is then its remainder will be zero.
        a.append(i)
for j in a:
    for k in range(2,j):
        if j%k==0:
            break
    else:
        b.append(j)
sorted(b)
print("the largest prime factor of the number is:",b[-1])