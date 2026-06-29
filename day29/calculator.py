while True:
    
    print("******** MENU-DRIVEN CALCULATOR ********")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Exponentiation")
    print("8. Exit")
    choice=int(input("enter the choice:-"))
    if choice==1:
        
        num1=int(input("\n ENTER THE FIRST NUMBER: "))
        num2=int(input("\n ENTER THE SECOND NUMBER: "))
        print("THE ADDITION OF THE TWO NUMBER IS :")
        print(num1+num2)
    elif choice==2:
        
        num1=int(input("\n ENTER THE FIRST NUMBER: "))
        num2=int(input("\n ENTER THE SECOND NUMBER: "))
        print("THE SUBTRACTION OF THE TWO NUMBER IS :")
        print(num1-num2)
    elif choice==3:
       
        num1=int(input("\n ENTER THE FIRST NUMBER: "))
        num2=int(input("\n ENTER THE SECOND NUMBER: "))
        print("THE MULTIPLICATION OF THE TWO NUMBER IS :")
        print(num1*num2)
    elif choice==4:
        
        num1=int(input("\n ENTER THE FIRST NUMBER: "))
        num2=int(input("\n ENTER THE SECOND NUMBER: "))
        if num2==0:
            print("DIVISON BY ZERO IS NOT POSSIBLE")
        else:
         print("THE DIVISION OF THE TWO NUMBER IS :")
         print(num1/num2)
    elif choice==5:
        
        num1=int(input("\n ENTER THE FIRST NUMBER: "))
        num2=int(input("\n ENTER THE SECOND NUMBER: "))
        if num2==0:
            print("MODULUS BY ZERO IS NOT POSSIBLE")
        else:
           print("THE MODULUS OF THE TWO NUMBER IS :")
           print(num1%num2)
    elif choice==6:
        
        num1=int(input("\n ENTER THE FIRST NUMBER: "))
        num2=int(input("\n ENTER THE SECOND NUMBER: "))
        if num2==0:
            print("FLOOR DIVISION BY ZERO IS NOT POSSIBLE")
        else:
         print("THE FLOOR DIVISION OF THE TWO NUMBER IS :")
         print(num1//num2)
    elif choice==7:
        num=int(input("ENTER THE NUMBER:-"))
        power=int(input("ENTER THE POWER:-"))  
        print("THE EXPONENTIATION IS:-")
        print(num**power)
    elif choice==8:
        print("THANK YOU!!")
        break
    else:
        print("INVALID CHOICE:-")
              