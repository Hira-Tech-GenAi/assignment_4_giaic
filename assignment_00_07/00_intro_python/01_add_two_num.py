
#? Write a program to add two numbers
#* Author: Hira Khalid
#* Date: 2022-10-11

def main()  -> None:
  print("\n***This program adds two numbers***\n")
  num_1: int = int(input("Enter first number: "))
  num_2: int = int(input("Enter second number: "))

  print(f"""First number is: {num_1} + Second number is: {num_2} = Total sum: {num_1 + num_2}""")

if __name__ == '__main__':
    main()