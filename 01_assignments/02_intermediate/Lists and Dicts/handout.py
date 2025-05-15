def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    # Slicing in Python doesn't raise IndexError, but we'll validate input anyway
    if start < 0 or end > len(lst) or start > end:
        return "Invalid indices."
    return lst[start:end]

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").lower()

    if operation == "access":
        try:
            index = int(input("Enter index to access: "))
            print("Value at index", index, ":", access_element(lst, index))
        except ValueError:
            print("Invalid input. Please enter an integer index.")

    elif operation == "modify":
        try:
            index = int(input("Enter index to modify: "))
            new_value = int(input("Enter new integer value: "))
            result = modify_element(lst, index, new_value)
            print("Modified list:", result)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    elif operation == "slice":
        try:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(lst, start, end)
            print("Sliced list:", result)
        except ValueError:
            print("Invalid input. Please enter integers.")

    else:
        print("Invalid operation. Please choose from: access, modify, or slice.")

index_game()
