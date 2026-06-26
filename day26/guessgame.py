import random
ch="y"
print("***************************WELCOME TO NUMBER GUESSING GAME****************************")
while ch=="y":
    num=random.randint(1,100)
    guess=0
    while True:
      print("GUESS THE NUMBER BETWEEN 1 TO 100 !!:-")
      n=int(input("CHOICE:-"))
      guess+=1
      if n>=1 and n<=100:
        if num==n:
            print("CONGRATULATIONS🥳🥳!! YOU GUESSED NUMBER👌👌")
            print(num)
            print("THE NUMBER OF GUESSES ARE:-")
            print(guess)
            break
        elif num<n:
            print("TOO HIGH!!😫")
        elif num>n:
            print("TOO LOW!!😔")
      else:
          print("PLEASE ENTER THE NUMBER BETWEEN 1 AND 100")
        
    print("ENTER 'Y' TO CONTINUE THE GAME AND 'N' TO EXIT THE GAME:-")
    ch=input().lower()
    if ch=="n":
        print("GAME OVER")
        break
    