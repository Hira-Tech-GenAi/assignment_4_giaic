# Ask the user to enter a number and convert it to an integer
curr_value = int(input("Enter a number: "))

# Double the number until it is 100 or more
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value)
