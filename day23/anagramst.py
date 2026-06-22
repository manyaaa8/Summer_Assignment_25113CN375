st1=input("ENTER THE FIRST STRING:-")
st2=input("ENTER THE SECOND STRING:-")
so_st1=sorted(st1.lower())
so_st2=sorted(st2.lower())
print(so_st1)
print(so_st2)
if so_st1==so_st2:
    print("IT IS A ANAGRAM STRING")
else:
    print("IT IS NOT A ANAGRAM STRING")