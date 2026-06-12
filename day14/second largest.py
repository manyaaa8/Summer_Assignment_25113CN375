from array import * #using the module
vals=array("i",[]) 
n=int(input("enter the number of elements you want to insert:-"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    vals.append(x) #method to insert the elements in array
lis=[]
for num in vals:
    if num not in lis: # if the element is not present then it will be appended in list
     lis.append(num)
# the above step is taken if we sort the list and there are two same elements then  it will give us wrong output
# as we use the index vals[-2]
lis.sort() # list method for sorting the list in ascending order
if len(lis)<2: # Checking the length of the list whether it has less the 2 element
    print("Second largest element does not exist")
else:
    print("The second largest element is:", lis[-2])
    