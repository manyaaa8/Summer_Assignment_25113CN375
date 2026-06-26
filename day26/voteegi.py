print("           ********** WELCOME TO VOTING ELIGIBILITY SYSTEM **********             ")
while True:
  print("1. FOR CHECKING THE AGE ELIGIBILITY  ")
  print("2. EXIT")
  try:
   choice=int(input("enter the choice:-"))
   if choice==1:
     print("ENTER THE NAME :- ")
     name=input()
     try:
      print("ENTER THE AGE :-")
      age=int(input())
      if age>0:
          if age>=18:
              print(name.upper(), "YOU ARE ELIGIBLE TO VOTE")
          else:
             print(name.upper(), "YOU ARE NOT ELIGIBLE TO VOTE ")
             print("YOU CAN VOTE AFTER ",18-age,"years") 
      else:
          print("AGE SHOULD NOT BE NEGATIVE ")
     except ValueError:
           print("INVALID CHOICE!! CHOOSE A INTEGER VALUE ")
   elif choice==2:
      print("THANK YOU FOR COMING")
      break
   else:
      print("INVALID CHOICE CHOOSE THE CORRECT OPTION")
  except ValueError:
       print("INVALID INPUT! PLEASE ENTER A NUMBER.")
    
