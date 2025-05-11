
def get_user_info() -> tuple[str, str, str]:
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    return first_name, last_name, email_address



def main() -> None:
    user_data: tuple[str, str, str] = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
    