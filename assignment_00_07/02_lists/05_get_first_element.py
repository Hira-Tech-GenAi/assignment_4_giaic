

def get_first_element(lst)-> None:
    """
    Prints the first element of a provided list.
    """

    print(lst[0])


def get_lst() -> list:
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst:list = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main()-> None:
    lst: list = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()

