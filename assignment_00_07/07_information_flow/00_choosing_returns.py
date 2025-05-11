# Define the age at which someone is considered an adult
ADULT_AGE = 18

# Function to check if the age is that of an adult
def is_adult(age)->bool:
    return age >= ADULT_AGE

# Test the function with user input
age = int(input("How old is this person?: "))
print(is_adult(age))
