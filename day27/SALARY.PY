print("        *********************** WELCOME TO SALARY MANAGEMENT SYSTEM *************************                 ")
salary_records = [
    [1001, "Rahul", 50000, 5000, 2000, 53000],
    [1002, "Priya", 60000, 6000, 3000, 63000]
]
def add_salary():
    employee_id= int(input("ENTER THE ID NUMBER : "))

    for i in salary_records:
        if i[0] == employee_id:
            print("Employee id already exists.")
            return
    # Continue only if emplyee id is unique
    name = input("NAME : ")
    salary = float(input("SALARY : "))
    bonus=float(input("BONUS : "))
    deduct=float(input("DEDUCTION : "))
    net_salary=salary+bonus-deduct
    salary_records.append([employee_id, name,salary,bonus,deduct,net_salary])
    print("SALARY DATA ADDED SUCCESSFULLY.")
def display_salary():
    print("****** EMPLOYEE'S SALARY RECORD ********")
    print("EMP_ID\tNAME\tSALARY\tBONUS\tDEDUCTION\tNET SALARY")
    for i in salary_records:
      for j in i:
          print(j,end="\t")
      print()
def search_salary():
    id=int(input("enter the employee id :-"))
    flag=0
    for i in salary_records :
        if i[0]==id:
            print(id,"is found and employee name is",i[1])
            print("EMPLOYEE ID :-",i[0])
            print("NAME:-",i[1])
            print("SALARY:-",i[2])
            print("BONUS:-",i[3])
            print("DEDUCE:-",i[4])
            print("NET SALARY:-",i[5])
            flag=1
            break
    if flag ==0:
            print(id,"is not found")
def update_salary():
    flag=0
    id=int(input("enter the emplyee_id: "))
    for i in salary_records:
        if i[0]==id:
            sal= float(input("ENTER THE NEW SALARY:-"))
            bonus= float(input("ENTER THE NEW BONUS:-"))
            deduce=float(input("ENTER THE NEW DEDUCE:-"))
            netsal=sal+bonus-deduce
            i[2]=sal
            i[3]=bonus
            i[4] =deduce
            i[5]=netsal
            print("EMPLOYEE'S SALARY DETAILS ARE UPDATED SUCCESSFULLY:-")
            flag=1
            break
    if flag ==0:
            print("NO EMPLOYEE IS FOUND WITH THIS ID",id)
    
def delete_salary():
    flag=0
    id=int(input("ENTER THE EMPLOYEE ID:-"))
    for i in salary_records:
        if i[0]==id:
            salary_records.remove(i)
            print("DELETED THE RECORD SUCCESSFULLY:-")
            flag=1
            break
    if flag==0:
            print("NO EMPLOYEE IS FOUND WITH THIS ID ",id)
        
while True:
    print("1.Add a employee salary record.")
    print("2.Display all employees salary records.")
    print("3.Search for a salary record by employee id.")
    print("4.Update a employee's salary details.")
    print("5.Delete a salary record.")
    print("6.Exit the program.")   
    choice=int(input("CHOOSE THE OPERATION FROM THR GIVEN OPTIONS:-"))
    if  choice==1:
        add_salary()
    elif choice==2:
        display_salary()
    elif choice==3:
        search_salary()
    elif choice==4:
        update_salary()
    elif choice==5:
        delete_salary()
    elif choice==6:
        print("EXITING THE PROGRAM....")
        break
    else:
        print("INVALID CHOICE")