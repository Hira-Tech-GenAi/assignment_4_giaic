
#?Write a program which asks the user what their favorite animal
#* Author: Hira Khalid
#* Date: 2022-10-11

def main() -> None:
    print("\n***This program asks the user what their favorite animal***\n")
    bold_italic = "\033[1;3m"
    color_reset = "\033[0m"

    animal: str = input(f"""{bold_italic}Enter your favorite animal: """)

    print(f"""Your favorite animal is: {animal}! {color_reset}""") 


if __name__ == '__main__':
    main()