print("        *********************** WELCOME TO STUDENT MANAGEMENT SYSTEM *************************                 ")
students = [
    [101, "Rahul", 20, "BCA", 85],
    [102, "Priya", 19, "B.Tech", 91]]
def add_student():
    roll_num = int(input("ENTER THE ROLL NUMBER : "))

    for i in students:
        if i[0] == roll_num:
            print("Roll Number already exists.")
            return
    # Continue only if roll number is unique
    name = input("NAME: ")
    age = int(input("AGE: "))
    course = input("COURSE: ")
    marks = float(input("MARKS: "))

    students.append([roll_num, name, age, course, marks])
    print("STUDENT ADDED SUCCESSFULLY.")
def display_student():
    print("****** STUDENT RECORD ********")
    print("ROLLNO\tNAME\tAGE\tCOURSE\tMARKS")
    for i in students:
      for j in i:
          print(j,end="\t")
      print()
def search_student():
    roll=int(input("enter the roll number of the student :-"))
    flag=0
    for i in students:
        if i[0]==roll:
            print(roll,"is found and student name is",i[1])
            print("ROLL NUMBER :-",i[0])
            print("NAME:-",i[1])
            print("AGE:-",i[2])
            print("COURSE:-",i[3])
            print("MARKS:-",i[4])
            flag=1
            break
    if flag ==0:
            print(roll,"is not found")
def update_student():
    flag=0
    roll=int(input("enter the roll number: "))
    for i in students:
        if i[0]==roll:
            name=input("ENTER THE NAME:-")
            age = int(input("ENTER THE NEW AGE:-"))
            course = input("ENTER THE NEW COURSE:-")
            marks = float(input("ENTER THE NEW MARKS:-"))
            i[1] = name
            i[2] = age
            i[3] = course
            i[4] = marks
            print("DATA UPDATED SUCCESSFULLY:-")
            flag=1
            break
    if flag ==0:
            print("NO STUDENT FOUND")
        

def delete_student():
    flag=0
    roll=int(input("ENTER THE ROLL NUMBER:-"))
    for i in students:
        if i[0]==roll:
            students.remove(i)
            print("DELETED RECORD SUCCESSFULLY:-")
            flag=1
            break
    if flag==0:
            print("NO STUDENT FOUND")
        
while True:
    print("1.Add a student record.")
    print("2.Display all student records.")
    print("3.Search for a student by Roll Number.")
    print("4.Update a student's details.")
    print("5.Delete a student record.")
    print("6.Exit the program.")   
    choice=int(input("CHOOSE THE OPERATION FROM THR GIVEN OPTIONS:-"))
    if  choice==1:
        add_student()
    elif choice==2:
        display_student()
    elif choice==3:
        search_student()
    elif choice==4:
        update_student()
    elif choice==5:
        delete_student()
    elif choice==6:
        print("EXITING THE PROGRAM....")
        break
    else:
        print("OPTION DOES NOT MATCH")