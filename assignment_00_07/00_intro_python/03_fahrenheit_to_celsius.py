
#? Temperature converted fahrenheit to Celsius.
#* Author: Hira Khalid
#* Date: 2022-10-11

def main()  -> None:
    print("\n***This program converts fahrenheit to celsius***\n")

    bold_italic = "\033[1;3m"
    color_reset = "\033[0m"

    fahrenheit: int = int(input(f""" {bold_italic}Enter temperature in fahrenheit: {color_reset}"""))

    celsius: float = (fahrenheit - 32) * 5 / 9

    print(f"""{fahrenheit}°F is {celsius:.2f} °C""")



if __name__ == '__main__':
    main()