
def main() -> None:
	num: int = 9
	num = subtract_seven(num)
	print("this should be zero: ", num)

def subtract_seven(num: int) -> int:
	num = num - 7
	return num



if __name__ == '__main__':
    main()