from array import *
arr=array("i",[8,6,7,5,4,2,1])
sum=int(input("enter the number whose pair is to be found:-"))
for i in range(len(arr)):
    for j in range(i+1, len(arr)):# i+1 is used to leave the element at i index so there is no same element addition 
         if arr[i] + arr[j] == sum: #comparing the addition of elements at i and j with the sum
            print("THE PAIRS ARE:-")
            print(arr[i], arr[j])
