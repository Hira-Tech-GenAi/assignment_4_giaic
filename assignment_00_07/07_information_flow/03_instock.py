
from typing import Literal


def main() -> None:
	fruit : str = input("Enter a fruit: ")
	stock: Literal[2] | Literal[4] | Literal[1000] | Literal[0] = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)


def num_in_stock(fruit) -> Literal[2] | Literal[4] | Literal[1000] | Literal[0]:
	"""
	This function returns the number of fruit Sophia has in stock.
	"""
	if fruit == 'apple':
		return 2
	if fruit == 'durian':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0


if __name__ == '__main__':
    main()