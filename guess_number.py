#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).



from art import guess_number_logo
import random
import os


picked_number = random.randint(1, 100)
game_on = True
EASY_LEVEL = 10
HARD_LEVEL = 5


while game_on:
    print(guess_number_logo)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user_input != "easy" and user_input != "hard":
        print("Please choose the right input.")
        game_on = False
    elif user_input == "easy":
        turns = EASY_LEVEL
    elif user_input == "hard":
        turns = HARD_LEVEL

    for i in range(turns):
        print(f"You have {turns-i} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))
        if guessed_number == picked_number:
            print(f"You guessed the right number: {picked_number}. You win!")
            game_on = False
            break
        elif guessed_number > picked_number:
            print("Too high.")
        elif guessed_number < picked_number:
            print("Too low.")
        if i == (turns-1):
            print("You've run out of guesses, you lose. \n")
    user_input2 = input("This repl has existed, run again? ")
    if user_input2 == "yes":
        os.system("clear")
        game_on = True
    else:
        game_on = False
