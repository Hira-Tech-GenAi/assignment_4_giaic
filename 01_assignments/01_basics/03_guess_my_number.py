import random

# Generate a random number between 0 and 99
secret_number = random.randint(0, 99)

# Ask the user to guess the number
guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

# Keep asking until the user guesses correctly
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    guess = int(input("Enter a new number: "))

# User guessed the correct number
print(f"Congrats! The number was: {secret_number}")
