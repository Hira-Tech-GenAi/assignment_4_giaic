
#?Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division


def main() -> None:
  first_number: int = int(input("\nEnter the first number: "))
  second_number: int = int(input("Enter the second number: "))

  print(f"{first_number} / {second_number} = {first_number / second_number}")
  print(f"{first_number} % {second_number} = {first_number % second_number}")

if __name__ == "__main__":
  main()