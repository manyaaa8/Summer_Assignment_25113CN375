print("******** STRING OPERATIONS SYSTEM ********")
st=""
def enter_st():
    global st
    st=input("Enter the strimg: ")
def display_st():
    if st=="":
        print("PEASE ENTER THE STRING!")
    else:
        print(st)
def length():
    if st=="":
        print("PLEASE ENTER THE STRING!")
    else:
        print("LENGTH OF STRING IS:")
        print(len(st))
def uppercase():
    global st
    if st=="":
        print("PLEASE ENTER THE STRING!")
    else:
      print("NOW THE STRING IS:")
      print(st.upper())
def lowercase():
    global st
    if st=="":
        print("PLEASE ENTER THE STRING!")
    else:
        print("NOW THE STRING IS: ")
        print(st.lower())
def reverse():
   if st=="":
        print("PLEASE ENTER THE STRING!")
   else: 
    print("THE REVERSE STRING IS:-")
    print(st[::-1])
def search():
    if st=="":
        print("PLEASE ENTER THE STRING!")
    else:
         char=input("ENTER THE CHARACTER TO BE SEARCHED: ")
         for i in st:
             if i==char:
                 print("THE ELEMENT IS FOUND")
                 return
         print("THE ELEMENT IS NOT PRESENT")
                 
def frequency():
    if st=="":
        print("PLEASE ENTER THE STRING!!")
    else:
      char_dic={}
      for i in st:
          if i not in char_dic:
             char_dic[i]=1
          else:
              char_dic[i]+=1
      for key,value in char_dic.items():
            print("the character:-", key ,"|| frequency:- ",value)
def replace():
    global st
    if st=="":
        print("PLEASE ENTER THE STRING!!")
    else:
       ch=input("enter the charcater to be replaced")
       new=input("enter the new character to be replace")
       word=st.replace(ch,new)
       if st==word:
           print("the character was not present")
       else:
          print("NEW STRING IS:-")
          st=word
          print(st)
def  palindrome():
  if st=="":
        print("PLEASE ENTER THE STRING!!")
  else:
     if st == st[::-1]:
      print("IT IS PALINDROME")
     else:
      print("IT IS NOT PALINDROME")
def remove_space():
    if st=="":
        print("PLEASE ENTER THE STRINg!!")
    else:
        a=st.replace(" ","")
        print("THE STRING AFTER REMOVING IS:-")
        print(a)
def count_words():
    if st=="":
        print("PLEASE ENTER THE STRING!!")
    else:
            word=st.split()
            count=0
            for i in word:
                 count+=1
            print("THE NUMBER OF WORDS:-",count)
def volcol():
    if st=="":
        print("PLEASE ENTER THE STRING!!")
    else:
        vol=0
        col=0
        for i in st:
          if i.isalpha():
           if i in "aeiouAEIOU":
            vol+=1
           else:
             col+=1
        print("THE NUMBER OF VOWELS IS:-") 
        print(vol)
        print("THE NUMBER OF CONSONANT IS:- ") 
        print(col)  

while True:
   
   print("\n1. Enter String")
   print("2. Display String")
   print("3. Find Length")
   print("4. Convert to Uppercase")
   print("5. Convert to Lowercase")
   print("6. Reverse String")
   print("7. Search Character/Substring")
   print("8. Count Character Frequency")
   print("9. Replace Character/Substring")
   print("10. Check Palindrome")
   print("11. Remove Spaces")
   print("12. Count Words")
   print("13. Count Vowels and Consonants")
   print("14. Exit")
   ch=int(input("enter the choice:"))
   if ch==1:
        enter_st()
   elif ch==2:
        display_st()
   elif ch==3:
        length()
   elif ch==4:
        uppercase()
   elif ch==5:
        lowercase()
   elif ch==6:
        reverse()
   elif ch==7:
        search()
   elif ch==8:
        frequency()
   elif ch==9:
        replace()
   elif ch==10:
        palindrome()
   elif ch==11:
        remove_space()
   elif ch==12:
        count_words()
   elif ch==13:
        volcol()
   elif ch==14:
        print("THANK YOU!!")
        break
   else:
        print("INVALID CHOICE!!")