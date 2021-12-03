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

#Write your code below this line 👇

games_image = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
    print("That is an invalid number you lose!")
else:

    print(games_image[choice])

    computer = random.randint(0, 2)
    print("Computer chose: \n" + games_image[computer])


    if choice == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and choice == 2:
        print("You lose!")
    elif computer > choice:
        print("you lose")
    elif choice > computer:
        print("You win")
    elif choice == computer:
        print("Draw")

#my attempt but its more code

# if choice == 0:
#     print(rock)
#     if computer == 0:
#         print("Computer Choice:\n " + rock)
#         print("Draw")
#     elif computer == 1:
#         print("Computer Choice:\n " + paper)
#         print("you lose!")
#     elif computer == 2:
#         print("Computer Choice:\n " + scissors)
#         print("You win!")
# elif choice == 1:
#     print(paper)
#     if computer == 0:
#         print("Computer Choice:\n " + rock)
#         print("You win!")
#     elif computer == 1:
#         print("Computer Choice:\n " + paper)
#         print("Draw")
#     elif computer == 2:
#         print("Computer Choice:\n " + scissors)
#         print("you lose!")
# elif choice  == 2:
#     print(scissors)
#     if computer == 0:
#         print("Computer Choice:\n " + rock)
#         print("you lose!")
#     elif computer == 1:
#         print("Computer Choice:\n " + paper)
#         print("You win!")
#     elif computer == 2:
#         print("Computer Choice:\n " + scissors)
#         print("Draw")
# else:
#     print("Not one of the options")

