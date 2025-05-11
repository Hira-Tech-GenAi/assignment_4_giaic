
#?Write a program to solve this age-related riddle!
#?Anton, Beth, Chen, Drew, and Ethan are all friends.
#* Author: Hira Khalid
#* Date: 2022-10-11

def main() -> None:
    print("\n***This program solves the age-related riddle***\n")

    bold_italic = "\033[1;3m"
    color_reset = "\033[0m"

    anton_age : int = 21  # Anton's age is given as 21 years old
    beth_age : int = 6 + anton_age  # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen_age : int = 20 + beth_age  # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew_age  : int= chen_age + anton_age  # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan_age : int = chen_age  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

#? Print out all of the ages!

    print(f"""{bold_italic}Anton is {anton_age} years old.{color_reset}""")

    print(f"""{bold_italic}Beth is {beth_age} years old.{color_reset}""")

    print(f"""{bold_italic}Chen is {chen_age} years old.{color_reset}""")

    print(f"""{bold_italic}Drew is {drew_age} years old.{color_reset}""")

    print(f"""{bold_italic}Ethan is {ethan_age} years old.{color_reset}""")





if __name__ == '__main__':
    main()

