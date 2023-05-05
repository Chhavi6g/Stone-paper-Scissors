#projet [Rock paper scissors]

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

user = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
if user>=3 or user<0:
    print("Invalid input")

else:
    if user==0:
        print(rock)
    elif user==1:
        print(paper)
    elif user==2:
        print(scissors)

    computer = random.randint(0,2)
    #print(computer)
    if computer==0:
        print("Computer chose:\n" + rock)
        if (computer==0) and(user==0):
            print("It's a tie")
        if (computer==0) and (user==1):
            print("You win!!")
        if (computer==0) and (user==2):
            print("You lose")
    
    elif computer==1:
        print("Computer chose:\n" + paper)
        if (computer==1) and(user==1):
            print("It's a tie")
        if (computer==1) and (user==0):
            print("You lose")
        if (computer==1) and (user==2):
            print("You win!!")
    
    else:
        print("Computer chose:\n" + scissors)
        if (computer==2) and(user==2):
            print("It's a tie")
        if (computer==2) and (user==0):
            print("You win!!")
        if (computer==2) and (user==1):
            print("You lose")



#or the same code can be written as ----

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_iamges=[rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))

if user>=3 or user<0:
    print("Invalid number, you lose!")
else:
    print(game_iamges[user])

    computer = random.randint(0,2)
    print("computer chose:")
    print(game_iamges[computer])



    if (computer==0) and (user==2):
        print("You lose!")
    elif  (user==0)and(computer==2) :
        print("You win!")
    elif computer > user:
        print("You lose!")
    elif computer < user:
        print("You win!")
    elif computer == user:
        print("It's a draw!")

        
