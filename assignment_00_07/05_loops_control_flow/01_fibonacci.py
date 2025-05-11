
#? Write a program to print terms in the Fibonacci sequence up to a maximum value.
MAX_TERM_VALUE : int = 10000

def main() -> None:
    curr_term = 0  #? The 0th Fibonacci Number
    next_term = 1  #? The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next: int   = curr_term + next_term
        curr_term= next_term
        next_term = term_after_next



if __name__ == '__main__':
    main()

    #?0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765