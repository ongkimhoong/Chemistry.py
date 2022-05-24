#!/usr/bin/env python

import random

def main():
    """Start guess one number or atomic at periodic table between table 1 and table 18."""
    print("Guess an atomic or number between table 1 and table 18 at periodic table!")

    atomicornumber = [
        "H" or "1",
        "He" or "2",
        "Li" or "3",
        "Be" or "4",
        "B" or "5",
        "C" or "6",
        "N" or "7",
        "O" or "8",
        "F" or "9",
        "Ne" or "10",
        "Na" or "11",
        "Mg" or "12",
        "Al" or "13",
        "Si" or "14",
        "P" or "15",
        "S" or "16",
        "Cl" or "17",
        "Ar" or "18"
        ]

    x = random.choice(atomicornumber)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What am i thinking the atomic or number now?"))

        if x == guess:
            print("You guessed {}. Congratulations your answer is correct!".format(guess))
            break
        else:
            print("You guessed {}. Oh no your answer is wrong please try again!".format(guess))

main()    

