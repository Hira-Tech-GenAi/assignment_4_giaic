
#?Write a function that takes a list of numbers and returns the sum of those numbers.

def add_many_numbers(numbers)->int:
  total = 0
  for number in numbers:
    total += number
  return total

def main() -> None:
  numbers:list[int] = [1, 2, 3, 4, 5]
  sum_of_numbers: int = add_many_numbers(numbers)
  print(sum_of_numbers)

if __name__ == "__main__":
  main()
