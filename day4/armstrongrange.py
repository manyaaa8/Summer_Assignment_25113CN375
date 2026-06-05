st=int(input("enter the starting range number")) 
ed=int(input("enter the ending range number"))
import math # we have use a module math to use the power fn in the program.
for i in range(st,ed+1): # ed +1  becuase to include the last number    
    temp=i 
    count=0
    dig=0
    while(temp!=0):
        temp=temp//10
        count+=1 # where we are counting the number of digit because we have to use it in power for the armstrong number.
    temp=i # here we have to assign temp as i because the value of temp is 0 after the above while loop.
    while (temp!=0):
      d=temp%10
      dig=dig+pow(d,count) # here power function is used for the armstrong number in the range as ut has different number of digits.
      temp=temp//10
    if (i==dig):
        print(i,"it is an armstron number")

        
        
            