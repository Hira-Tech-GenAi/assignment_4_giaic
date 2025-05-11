
#?Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!
"""
Here's a sample run of the program (user input is in blue):

Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

Note that you can call input() with no prompt and it will still wait for a user to type something!"""
from colorama import Fore, Style

AFFIRMATION : str = Fore.BLUE + "I am capable of doing anything I put my mind to." + Style.RESET_ALL

def main() -> None:
    print(Fore.YELLOW + "Please type the following affirmation: " + Style.RESET_ALL + AFFIRMATION)

    user_feedback: str = input()  #? Get user's input
    while user_feedback != AFFIRMATION:  #? While the user's input isn't the affirmation
        #? Tell the user that they did not type the affirmation correctly
        print(Fore.RED + "That was not the affirmation." + Style.RESET_ALL)

        #? Ask the user to type the affirmation again!
        print(Fore.YELLOW + "Please type the following affirmation: " +Style.RESET_ALL + AFFIRMATION)
        user_feedback = input()

    print(Fore.GREEN + "That's right! :)" + Style.RESET_ALL)




if __name__ == '__main__':
    main()