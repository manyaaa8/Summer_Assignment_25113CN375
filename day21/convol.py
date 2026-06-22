st=input("enter the string:-")
vol=0
col=0
for i in st:
    if i in "aeiouAEIOU":
      vol+=1
    else:
        col+=1
print("THE NUMBER OF VOWELS IS:-") 
print(vol)
print("THE NUMBER OF CONSONANT IS:- ") 
print(col)  
