
#?Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

#* Import the random library which lets us simulate random things like dice!
import random

DICE_SIDES: int = 6

def dice_roll() -> None:
  """
  Simulates rolling two dice and prints their total
  """
  die1: int = random.randint(1, DICE_SIDES)
  die2: int = random.randint(1, DICE_SIDES)
  total: int = die1 + die2
  print("Total of two dice:", total)


def main() -> None:
  for _ in range(3):
    dice_roll()


if __name__ == "__main__":
  main()