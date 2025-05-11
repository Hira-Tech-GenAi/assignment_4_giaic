
#?Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

#?E = m * c**2

C: int = 299792458  #? The speed of light in m/s
def main() -> None:
  print(f"""
  Welcome to the energy calculator!
    This program will calculate the energy of an object""")

  bold_italic = "\033[1m\033[3m"
  reset = "\033[0m"

  while True:
    try:
      mass_in_kg: float = float(input("Enter the mass of the object in kilograms: "))
      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  energy: float = mass_in_kg * (C**2)
  print("e = m * C^2...")
  print("m = " + str(mass_in_kg) + " kg")
  print("C = " + str(C) + " m/s")
  print(f"The energy of the object is {bold_italic}{energy:.2e}{reset} joules.")



if __name__ == '__main__':
    main()