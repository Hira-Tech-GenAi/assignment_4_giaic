
#?Print 10 random numbers in the range 1 to 100.


import random

def main() -> None:
    #? Prompt the user to enter a range choice
    user_input = int(input("Enter the range (1, 10, or 100): "))

    #? Check the user input and print numbers in the specified range
    if user_input == 1:
        print("Numbers in range 1 to 1:")
        print(*range(1, 2), sep=", ")
    elif user_input == 10:
        print("Numbers in range 1 to 10:")
        print(*range(1, 11), sep=", ")
    elif user_input == 100:
        print("Numbers in range 1 to 100:")
        print(*range(1, 101), sep=", ")
    else:
        print("Invalid input! Please enter 1, 10, or 100.")

if __name__ == '__main__':
    main()


