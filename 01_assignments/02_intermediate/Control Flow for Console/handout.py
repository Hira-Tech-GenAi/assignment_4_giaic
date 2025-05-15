import random

NUM_ROUNDS = 5  # You can set this to any number of rounds you want

print("Welcome to the High-Low Game!")
print("--------------------------------")

score = 0

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")

    computer_number = random.randint(1, 100)
    your_number = random.randint(1, 100)
    print(f"Your number is {your_number}")

    # Get user input with input validation
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either 'higher' or 'lower': ").lower()

    # Determine win/loss
    if your_number == computer_number:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    elif (guess == "higher" and your_number > computer_number) or (guess == "lower" and your_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

    print(f"Your score is now {score}")
    print()  # Blank line between rounds

# Final evaluation message
print("Game Over!")
print(f"Your final score is {score} out of {NUM_ROUNDS}")

if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
