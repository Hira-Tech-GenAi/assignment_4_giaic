
"""Fill out the function count_even(lst) which

first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

and then prints the number of even numbers in the list.

If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!"""


def count_even(lst) -> None:
 
    count = 0  #? Stores the count of even numbers in the list
    for num in lst:  #? Loop through the numbers in the list
        if num % 2 == 0:  # ?If the current number in the list is even (divisible by 2)
            count += 1  #? Add one to our count!

    print(f"There are {count} even numbers in the list.")

def get_list_of_ints()->list:
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst:list = []  # ?Make an empty list to store integers
    user_input:str = input("Enter an integer or press enter to stop: ")  #? Get user input for an integer
    while user_input != "":  # ?While the user doesn't enter nothing...
        lst.append(int(user_input))  #? Cast the user input into an integer and add it to our list
        user_input = input("Enter an integer or press enter to stop: ")  # ?Get the next user input

    return lst

def main() -> None:
    lst:list = get_list_of_ints()
    count_even(lst)
    print(lst)
  
    print("I'm done.")

if __name__ == '__main__':
    main()