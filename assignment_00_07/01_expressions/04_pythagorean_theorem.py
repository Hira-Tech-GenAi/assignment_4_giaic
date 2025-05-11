
#?Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

import math  #* Import the math library so we can use the sqrt function

def main() -> None:
  a_b:float = float(input("Enter the length of side AB: "))
  b_c:float = float(input("Enter the length of side BC: "))
  c:float = math.sqrt(a_b**2 + b_c**2)  #* The sqrt function returns the square root

  print(f"The length of side c is {c:.2f}")


if __name__ == '__main__':
  main()