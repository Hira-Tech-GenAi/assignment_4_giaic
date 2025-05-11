
#create a function that returns a greeting

def main() -> None:
  input_name: str = input("What is your name? ")
  print(greet(input_name))


def greet(name: str) -> str:
  return f"Hello, {name}!"    


if __name__ == "__main__":
  main()

