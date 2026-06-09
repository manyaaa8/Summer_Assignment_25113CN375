def prime(n,flag=0):

    for i in range(2, n):
        if n % i == 0:
            flag = 1
            break

    if flag == 1:
        print(f"The number {n} is not prime")
    else:
        print(f"The number {n} is prime")

n = int(input("Enter the number to be checked: "))
prime(n)