from art import guess_number_logo
import random
# from


picked_number = random.randint(1, 100)
game_on = True

# def guess(num):
#     if num == picked_number:
#         print("You guessed the right number: {picked_number}. You win!")
#     elif num > picked_number:
#         print("Too high. \nGuess again.")
#     elif num < picked_number:
#         print("Too low. \nGuess again.")


def display():
    print(f"You have {attempts} attempts remaining to guess the number.")
    global guessed_number
    guessed_number = int(input("Make a guess: "))



while game_on:
    print(guess_number_logo)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user_input != "easy" and user_input != "hard":
        print("Please choose the right input.")
        game_on = False
    elif user_input == "easy":
        attempts = 10
    elif user_input == "hard":
        attempts = 5
    for i in range(attempts):
        display()
        if guessed_number == picked_number:
            print(f"You guessed the right number: {picked_number}. You win!")
            game_on = False
        elif guessed_number > picked_number:
            print("Too high. \nGuess again.")
        elif guessed_number < picked_number:
            print("Too low. \nGuess again.")
        attempts -= 1
    print("You've run out of guesses, you lose. \n")
    user_input2 = input("This repl has existed, run again?")
    if user_input2 == "yes":
        game_on = True
    else:
        game_on = False
