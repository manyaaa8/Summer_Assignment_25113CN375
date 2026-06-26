st1 = input("ENTER THE FIRST STRING: ")
st2 = input("ENTER THE SECOND STRING: ")
if len(st1) != len(st2):
    print("NOT A ROTATION")
elif st2 in (st1 + st1):
    print("ROTATION")
else:
    print("NOT A ROTATION")