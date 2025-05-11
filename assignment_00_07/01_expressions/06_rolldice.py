
#?Simulate rolling two dice, and prints results of each roll as well as the total.

#* Import the random library which lets us simulate random things like dice!
import random
"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

DICE_SIDES: int = 6

def main() -> None:
  """
  Simulates rolling two dice and prints their total
  """
  die1: int = random.randint(1, DICE_SIDES)
  die2: int = random.randint(1, DICE_SIDES)
  total: int = die1 + die2
  print("Total of two dice:", total)


if __name__ == "__main__":
  main()