# Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess.
# If the user guesses wrong then the prompt appears again until the guess is correct,
# on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random

ra = random.randint(1,9)

should_continue = True
while should_continue:
    n = int(input("guess a digit: ").title())
    if n == ra:
        print("Well guessed!")
        should_continue = False
    else:
        print("wrong guess! try again")
