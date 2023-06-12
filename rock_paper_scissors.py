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
options = [rock, paper, scissors]
choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

if choice >= 3 or choice < 0:
    print("You typed invalid choice. You lose!")
else:
    print(options[choice])
    comp_choice = random.randint(0, 2)
    print("Computer chose:\n" + options[comp_choice])
    if choice == comp_choice:
        print("Its a draw. Play again!")
    elif choice == 0:
        if comp_choice == 1:
            print("You lose!")
        elif comp_choice == 2:
            print("You won!")
    elif choice == 1:
        if comp_choice == 2:
            print("You lose!")
        if comp_choice == 0:
            print("You won!")
    elif choice == 2:
        if comp_choice == 1:
            print("You won!")
        if comp_choice == 0:
            print("You lose!")
