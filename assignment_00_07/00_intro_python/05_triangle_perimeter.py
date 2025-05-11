
#?Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
#* Author: Hira Khalid
#* Date: 2022-10-11


def main() -> None:
  print("\n***This program calculates the perimeter of a triangle***\n")

  bold_italic = "\033[1;3m"
  color_reset = "\033[0m"

  side_1: float = float(input(f"""{bold_italic}Enter length of side 1: {color_reset}"""))
  side_2: float = float(input(f"""{bold_italic}Enter length of side 2: {color_reset}"""))
  side_3: float = float(input(f"""{bold_italic}Enter length of side 3: {color_reset}"""))

  print(f"""The perimeter of the triangle is: {side_1 + side_2 + side_3}\n""")


if __name__ == "__main__":
  main()