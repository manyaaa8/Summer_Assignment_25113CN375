ques=["1. What is the capital of India?",
      "2. Who is known as the Father of the Nation in India?",
      "3. Which is the largest planet in our Solar System?",
      "4. Which is the longest river in the world?",
      "5. Which is the national animal of India?"]
      
choice=[ 
        ["A) Mumbai","B) Chennai","C) New Delhi","D) Kolkata"],
        ["A) Jawaharlal Nehru","B) Mahatma Gandhi","C) Bhagat Singh","D) Sardar Patel"],
        ["A) Earth","B) Mars","C) Jupiter","D) Saturn"],
        ["A) Ganga","B) Amazon","C) Nile","D) Yangtze"],
        ["A) Lion","B) Elephant","C) Tiger","D) Leopard"]
        ]

answer=[ "C","B","C","C","C"]
play_choice=[]
correct=0
wrong=0

print("***************** WELCOME TO THE QUIZ ************************")

print("\n**📜 QUIZ RULES**")
print("\n1. The quiz consists of multiple-choice questions (MCQs).")
print("2. Each question has four options: A, B, C, and D.")
print("3. Read each question carefully before answering.")
print("4. Enter only the correct option (A, B, C, or D).")
print("5. Each correct answer carries **1 mark**.")
print("6. There is **no negative marking** for wrong answers.")
print("7. You cannot change your answer after submitting it.")
print("8. Invalid inputs will be treated as incorrect answers.")
print("9. Your final score will be displayed after all questions are completed.")
print("10.Try to answer all questions honestly without any external help.")
print("11.Have fun and do your best!")
print("**Best of Luck!!**")
  
print("\n LET US BEGIN THE QUIZ!!")
for i in range(len(ques)):
    print("\n", ques[i])

    for option in choice[i]:
        print(option)

    user_answer = input("ENTER YOUR ANSWER (A/B/C/D): ").upper()
    play_choice.append(user_answer)

    if user_answer == answer[i]:
        print("CORRECT ANSWER!")
        correct += 1
    else:
        print("WRONG ANSWER!")
        print("CORRECT ANSWER IS:", answer[i])
        wrong += 1
print("\n FINAL SCORES:-")
print("\n CORRECT ANSWERS:",correct)
print(" WRONG ANSWERS:",wrong)
    
        
