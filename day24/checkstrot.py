st=input("enter the string:-")
word=st.split(" ")
longest=word[0]
for i in word:
    if len(i)>len(longest):
        longest=i
print("the longest word is",longest)