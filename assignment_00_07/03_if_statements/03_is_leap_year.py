
#?Write a program that reads a year from the user and tells whether a given year is a leap year or not.



def main() -> None:
    #? Get the year to check from the user
    year = int(input('Please input a year: '))

    if year % 4 == 0:  
        if year % 100 == 0:  
            if year % 400 == 0:  
                print("That's a leap year!")
            else:  #? (Not divisible by 400)
                print("That's not a leap year.")
        else:  #? (Not divisible by 100)
            print("That's a leap year!")
    else:  # ?(Not divisible by 4)
        print("That's not a leap year.")



if __name__ == '__main__':
    main()