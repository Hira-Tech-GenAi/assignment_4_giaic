# Gravity constants relative to Earth's gravity
MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 1.06
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.19

# Prompt the user for their weight on Earth
earth_weight = float(input("Enter your weight on Earth (in kg): "))

# Prompt the user for the name of a planet
planet = input("Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")

# Determine the gravitational constant for the selected planet
if planet == "Mercury":
    gravity_constant = MERCURY_GRAVITY
elif planet == "Venus":
    gravity_constant = VENUS_GRAVITY
elif planet == "Mars":
    gravity_constant = MARS_GRAVITY
elif planet == "Jupiter":
    gravity_constant = JUPITER_GRAVITY
elif planet == "Saturn":
    gravity_constant = SATURN_GRAVITY
elif planet == "Uranus":
    gravity_constant = URANUS_GRAVITY
else:
    # Assuming the user inputs a valid planet from the list
    gravity_constant = NEPTUNE_GRAVITY

# Calculate the equivalent weight on the selected planet
planetary_weight = earth_weight * gravity_constant
rounded_planetary_weight = round(planetary_weight, 2)

# Print the result
print("The equivalent weight on " + planet + ": " + str(rounded_planetary_weight) + " kg")
