
#? Write a program that doubles each element in a list of numbers. For example, if you start with this list
#? [1, 2, 3, 4, 5], it should end up as [2, 4, 6, 8, 10].

def double_list(numbers: list[int]) -> list[int]:

  doubled_list: list[int]   = []

  for number in numbers:
    doubled_list.append(number * 2)
  return doubled_list

def main() -> None:
  numbers: list[int] = [1, 2, 3, 4, 5]
  doubled_list: list[int] = double_list(numbers)
  print(doubled_list)   

if __name__ == "__main__":
  main()