from array import * #using the module
vals=array("i",[]) 
n=int(input("enter the number of elements you want to insert:-"))
for i in range(0,n):
    x=int(input("enter the element:-"))
    vals.append(x) #method to insert the elements in array
dic={} # dictionary contains the key value pairs so it will be easy to know the frequency.
for num in vals:
    if num not in dic: # if the element is not present then it has value 1 ,as the keys should be unique in dictonary
     dic[num]=1
    else:
        dic[num]+=1 # if the element is present , then we simply increase the value by 1
for key,values in dic.items(): # dictionary method is used for printing the key value as item contains list of tuples
    print("Element:",key,"|| Frequency:",values)
    