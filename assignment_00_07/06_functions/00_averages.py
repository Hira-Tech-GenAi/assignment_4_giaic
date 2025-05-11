
#?Write a function that takes two numbers and finds the average between the two.

def average(num1, num2)->float:
  """Returns the average between two numbers"""
  return (num1 + num2) / 2

def main()->None:
  result: float = average(5, 10)
  print(f"""{result:.2f}""")


if __name__ == "__main__":
  main()