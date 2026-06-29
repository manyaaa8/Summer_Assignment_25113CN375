from array import *
arr=array("i",[])
def insert():
    print("a.YOU WANT TO INSERT ELEMENT AT END")
    print("b.YOU WANT TO INSERT AT A PARTICULAR POSITION")
    ch1=input("CHOOSE THE OPTON:-").lower()
    num=int(input("ENTER THE ELEMENT:-"))
    if len(arr)==0:
        print("THE ARRAY IS EMPTY SO THE ELEMENT WILL WE INSERTES AT THE FIRST POSITION")
        arr.append(num)
    else:
        if ch1=="a":
            arr.append(num)
        elif ch1=="b":
            pos=int(input("ENTER THE POSITION OF THE ELEMENT YOU WANT TO INSERT: "))
            if pos >= 0 and pos <= len(arr):
                arr.insert(pos, num)
            else:
                print("INVALID POSITION")
        else:
            print("THE ELEMENT WILL BE ADDED IN THE END OF ARRAY")
            arr.append(num)
def display():
    if len(arr)==0:
        print("ARRAY IS EMPTY")
    else:
     for i in arr:
        print(i,end=" ")
     print()
def search():
    ele=int(input("enter the element you want to search:-"))
    if len(arr)==0:
        print("ARRAY IS EMPTY:")
    else:
        for i in range(len(arr)):
          if arr[i]==ele:
             print("ELEMENT IS FOUND AT POSITION ",i)
             return
        print("ELEMENT IS NOT PRESENT IN THE ARRAY")
def update():
    old_ele=int(input("enter the old element: "))
    new_ele=int(input("enter the new element: "))
    if len(arr)==0:
        print("ARRAY IS EMPTY:")
    else:
     for i in range(len(arr)):
        if arr[i]==old_ele:
            arr[i]=new_ele
            print("ELEMENT UPDATED SUCESSFULLY!!")
            return
    
     print("ELEMENT NOT FOUND")          
def delete():
    ele=int(input("enter the old element: "))
    if len(arr)==0:
        print("ARRAY IS EMPTY:")
    else:
     for i in range(len(arr)):
        if arr[i]==ele:
            arr.remove(ele)
            print("ELEMENT DELETED SUCCESSFULLY!!")
            return
     print("ELEMENT NOT FOUND!!")
def max_element():
    if len(arr)==0:
        print("ARRAY IS EMPTY:")
    else:
     print("THE MAXIMUM ELEMENT IS: ")
     print(max(arr))
def min_element():
    if len(arr)==0:
        print("ARRAY IS EMPTY:")
    else:
     print("THE MINIMUM ELEMENT IS: ")
     print(min(arr))
def sum_element():
    if len(arr)==0:
        print("ARRAY IS EMPTY:")
    else:
     print("THE SUM OF ELEMENTS IS:")
     print(sum(arr))
def avg():
    if len(arr)==0:
        print("ARRAY IS EMPTY:")
    else:
     total=sum(arr)
     average=total/len(arr)
     print("THE AVERAGE OF ELEMENTS: ")
     print(average)
def sort_arr():
    if len(arr)==0:
        print("ARRAY IS EMPTY:")
        return
    else:
        for i in range(0,len(arr)-1):
            for j in range(0,len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        print("ARRAY SORTED SUCCESSFULLY")
                    
def reverse_arr():
   if len(arr) == 0:
      print("ARRAY IS EMPTY")
      return
   else:
      low=0
      high=len(arr)-1
      while low<=high:
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high=high-1        
def count():
   if len(arr) == 0:
      print("ARRAY IS EMPTY")
   else: 
      print("NUMBER OF ELEMENT PRESENT ARE:-")
      print(len(arr))
    
print("******** ARRAY OPERATIONS SYSTEM ********")  

while True:

    print("1. Insert Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Update Element")
    print("5. Delete Element")
    print("6. Find Maximum")
    print("7. Find Minimum")
    print("8. Calculate Sum")
    print("9. Calculate Average")
    print("10. Sort Array")
    print("11. Reverse Array")
    print("12. Count Elements")
    print("13. Exit")
    ch=int(input("enter the choice:"))
    if ch==1:
        insert()
    elif ch==2:
        display()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
        max_element()
    elif ch==7:
        min_element()
    elif ch==8:
        sum_element()
    elif ch==9:
        avg()
    elif ch==10:
        sort_arr()
    elif ch==11:
        reverse_arr()
    elif ch==12:
        count()
    elif ch==13:
        print("THANK YOU!!")
        break
    else:
        print("INVALID CHOICE!!")