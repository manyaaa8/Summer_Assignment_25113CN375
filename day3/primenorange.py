st= int(input("enter the starting range number"))
ed = int(input("enter the ending range number"))

for j in range(st, ed + 1):
 prime = 0
 if j>1:
    for i in range(2, j):
        if j % i == 0:
            prime = 1
            break

    if prime == 0:
        print(j, "is prime number")
 
    