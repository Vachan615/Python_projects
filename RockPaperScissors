#Rock Paper Scissors
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

choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("You chose:\n")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Wrong choice\n")


print("Computer chose:\n ")
list_of_rps=[0,1,2]
computer=random.choice(list_of_rps)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

if choice == computer:
    print("It's a draw")
elif choice == 0 and computer == 1:
    print("Computer wins")
elif choice == 0 and computer == 2:
    print("You win")
elif choice == 1 and computer == 0:
    print("You win")
elif choice == 1 and computer == 2:
    print("Computer wins")
elif choice == 2 and computer == 0:
    print("Computer wins")
else:
    print("You win")

