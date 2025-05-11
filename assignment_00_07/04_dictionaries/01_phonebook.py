#? In this program we show an example of using dictionaries to keep track of information in a phone book

from colorama import Fore, Style
def read_phone_numbers()->dict:
    """
    Ask the user for names/numbers to story in a phone book (dictionary).
    Returns the phone book.
    """
    phone_book: dict = {}                   #? Create empty phone book

    while True:
        name: str = input(Fore.BLUE + "🤵 Name: " + Style.RESET_ALL)
        if name == "":
            break
        number: str = input(Fore.GREEN + "📳Number: " + Style.RESET_ALL)
        phone_book[name] = number

    return phone_book


def print_phone_book(phone_book) -> None:
    """
    Prints out all the names/numbers in the phone book.
    """
    for name in phone_book:
        print(str(name) + " -> " + str(phone_book[name]))


def lookup_numbers(phone_book) -> None:
    """
    Allow the user to lookup phone numbers in the phone book
    by looking up the number associated with a name.
    """
    while True:
        name: str = input(Fore.YELLOW + "Enter name to lookup: " + Style.RESET_ALL)
        if name == "":
            break
        if name not in phone_book:
            print(Fore.RED + name + " is not in the phone_book" + Style.RESET_ALL)
        else:
            print(phone_book[name])


def main() -> None:
    phone_book: dict = read_phone_numbers()
    print_phone_book(phone_book)
    lookup_numbers(phone_book)


#? Python boilerplate.
if __name__ == '__main__':
    main()