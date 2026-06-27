print("         ******************* MARKSHEET GENERATION SYSTEM  **********************           " )
roll_no=int(input("ENTER THE ROLL NO. : "))
name=input("ENTER YOUR NAME : ")
print("-----------ENTER THE MARKS FOR THE SUBJECTS-----------      ")
eng=float(input("ENTER THE MARKS FOR ENGLISH :"))
math=float(input("ENTER THE MARKS FOR MATHEMATICS : "))
physics=float(input("ENTER THE MARKS FOR PHYSICS : "))
chem=float(input("ENTER THE MARKS FOR CHEMISTRY : "))
cs=float(input("ENTER THE MARKS FOR COMPUTER SCIENCE : "))
total=eng+math+physics+chem+cs
per=total/5
if eng>=33 and math>=33 and physics>=33 and chem>=33 and cs>=33:
    result="PASS"
else:
    result="FAILED"
if result=="FAILED":
    grade="F"
else:
    if per>=90:
        grade="A+"
    elif per>=80:
        grade="A"
    elif per>=70:
        grade="B"
    elif per>=60:
        grade="C"
    elif per>=50:
        grade="D"
    else:
        grade="F"
print("-------------------------------------------------------------")
print("                      STUDENT MARKSHEET                      ")
print("-------------------------------------------------------------")
print("ROLL NO     :",roll_no)
print("NAME        :",name)
print("ENGLISH     :",eng)
print("MATHEMATICS :",math)
print("PHYSICS     :",physics)
print("CHEMISTRY   :",chem)
print("COMPUTER SCI:",cs)
print("TOTAL MARKS :",total)
print("PERCENTAGE  :",per)
print("GRADE       :",grade)
print("RESULT      :",result)
print("---------------------------------------------------------------")