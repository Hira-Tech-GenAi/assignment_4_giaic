
#?Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

def main() -> None:
    lst: list[str] = []  # Make an empty list to store things in

    val:str = input("Enter a value: ")  
    while val: 
        lst.append(val) # Add val to list
        val = input("Enter a value: ")  

    print("Here's the list:", lst)




if __name__ == '__main__':
    main()