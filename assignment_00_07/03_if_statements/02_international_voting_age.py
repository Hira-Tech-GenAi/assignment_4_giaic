
#? Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
#*Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different. In Peturksbouipo, the voting age is 21. In Mayengua, the voting age is 18. In Stanlau, the voting age is 17.

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main() -> None:
    
    user_age = int(input("How old are you? "))

    
    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    
    
    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    
    
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")



if __name__ == '__main__':
    main()
