
def add_three_copies(my_list, data) -> None:
    for i in range(3):
        my_list.append(data)



def main() -> None:
    message: str = input("Enter a message to copy: ")
    my_list: list[str] = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()