
#? Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!


SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb


def main() -> None:

  print("Let's make a sentence!")

  bold_italic = "\033[1m\033[3m"
  reset = "\033[0m"

  adjective: str = input(f"""{bold_italic}Enter an adjective: {reset}""")

  noun: str = input(f"""{bold_italic}Enter a noun: {reset}""")

  verb: str = input(f"""{bold_italic}Enter a verb: {reset}""")


  sentence: str = SENTENCE_START + adjective + " " + noun + " " + verb
  print(sentence)

if __name__ == "__main__":
  main()