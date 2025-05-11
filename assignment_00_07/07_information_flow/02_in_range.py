#Implement the following function which takes in 3 integers as parameters:

#def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def main () -> None:
  n = int(input("Enter an integer: "))
  low = int(input("Enter a lower bound: "))
  high = int(input("Enter an upper bound: "))
  print(in_range(n, low, high))


def in_range(n, low, high) -> bool:
  if n >= low and n <= high:
    return True
  else:
    return False


if __name__ == "__main__":
  main()