print("        *********************** WELCOME TO EMPLOYEE MANAGEMENT SYSTEM *************************                 ")
employees = [
    [1001, "Rahul", "HR", 35000],
    [1002, "Priya", "IT", 50000]
]
def add_employee():
    employee_id= int(input("ENTER THE ID NUMBER : "))

    for i in employees:
        if i[0] == employee_id:
            print("Employee id already exists.")
            return
    # Continue only if emplyee id is unique
    name = input("NAME: ")
    department = input("DEPARTMENT: ")
    salary = float(input("SALARY: "))

    employees.append([employee_id, name,department,salary])
    print("EMPLOYEE DATA ADDED SUCCESSFULLY.")
def display_employee():
    print("****** EMPLOYEE'S RECORD ********")
    print("EMP_ID\tNAME\tDEPARTMENT\tSALARY")
    for i in employees:
      for j in i:
          print(j,end="\t")
      print()
def search_employee():
    id=int(input("enter the employee id :-"))
    flag=0
    for i in employees:
        if i[0]==id:
            print(id,"is found and employee name is",i[1])
            print("EMPLOYEE ID :-",i[0])
            print("NAME:-",i[1])
            print("DEPARTMENT:-",i[2])
            print("SALARY:-",i[3])
            flag=1
            break
    if flag ==0:
            print(id,"is not found")
def update_employee():
    flag=0
    id=int(input("enter the emplyee_id: "))
    for i in employees:
        if i[0]==id:
            name=input("ENTER THE NAME:-")
            department = input("ENTER THE NEW DEPARTMENT:-")
            salary= float(input("ENTER THE NEW SALARY:-"))
            i[1] = name
            i[2]=department
            i[3] = salary
            print("EMPLOYEE DETAILS UPDATED SUCCESSFULLY:-")
            flag=1
            break
    if flag ==0:
            print("NO EMPLOYEE IS FOUND WITH THIS ID",id)
    
def delete_employee():
    flag=0
    id=int(input("ENTER THE EMPLOYEE ID:-"))
    for i in employees:
        if i[0]==id:
            employees.remove(i)
            print("DELETED THE RECORD SUCCESSFULLY:-")
            flag=1
            break
    if flag==0:
            print("NO EMPLOYEE IS FOUND WITH THIS ID ",id)
        
while True:
    print("1.Add a employeee record.")
    print("2.Display all employee records.")
    print("3.Search for a employee by employee id.")
    print("4.Update a employee's details.")
    print("5.Delete a employee record.")
    print("6.Exit the program.")   
    choice=int(input("CHOOSE THE OPERATION FROM THR GIVEN OPTIONS:-"))
    if  choice==1:
        add_employee()
    elif choice==2:
        display_employee()
    elif choice==3:
        search_employee()
    elif choice==4:
        update_employee()
    elif choice==5:
        delete_employee()
    elif choice==6:
        print("EXITING THE PROGRAM....")
        break
    else:
        print("OPTION DOES NOT MATCH")