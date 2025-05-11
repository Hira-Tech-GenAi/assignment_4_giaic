"""
There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs."""
from colorama import Fore, Style
def main() -> None:
    fruits: dict = {'apple': 1.5, 'lichi': 50, 'dragonfruit': 80, 'kiwi': 1, 'orange': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price: int = fruits[fruit_name]
        amount_bought = int(input(Fore.YELLOW + "How many (" + fruit_name + ") do you want to buy?: " + Style.RESET_ALL))
        total_cost += (price * amount_bought)
    
    print("Your total is 💲"  + str(total_cost))




if __name__ == '__main__':
    main()