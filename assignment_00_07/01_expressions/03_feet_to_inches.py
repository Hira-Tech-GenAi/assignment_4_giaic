
#? Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


inches_per_foot: int = 12  #* There are 12 inches for 1 foot.

def main() -> None:
  feet:float = float(input("\nEnter the number of feet: "))
  inches:float = feet * inches_per_foot
  print(f"{feet:.2f} feet is {inches:.2f} inches.")


if __name__ == '__main__':
  main()