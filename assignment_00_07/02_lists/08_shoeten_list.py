
#?Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long.

MAX_LENGTH : int = 3

def shorten(lst) -> None:
    while len(lst) > MAX_LENGTH:
        last_elem: str = lst.pop()
        print(last_elem)




def get_lst()->list:
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst:list = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main() -> None:
    lst: list = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()