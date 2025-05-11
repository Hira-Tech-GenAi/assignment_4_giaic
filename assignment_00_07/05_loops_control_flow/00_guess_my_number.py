
#? I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
"""
Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48"""

import random
from colorama import Fore, Style

def main() -> None:
    #? Generate the secret number at random!
    secret_number: int = random.randint(1, 99)
    
    print("🧐 I am thinking of a number between 1 and 99...")
    
    #? Get user's guess
    guess = int(input(Fore.GREEN + "Enter a guess: " + Style.RESET_ALL))
    #? True if guess is not equal to secret number
    while guess != secret_number:
        if guess < secret_number:  # ?If-statement is True if guess is less than secret number
            print(Fore.YELLOW + "Your guess is too low" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Your guess is too high" + Style.RESET_ALL)
            
        print() # ?Print an empty line to tidy up the console for new guesses
        guess = int(input(Fore.GREEN + "Enter a new guess: " + Style.RESET_ALL))  #? Get a new guess from the user
        
    print(Fore.BLUE + "🥳 Congrats! The number was: " + Style.RESET_ALL + str(secret_number))
    
if __name__ == '__main__':
    main()