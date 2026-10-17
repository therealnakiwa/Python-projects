# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:38:27 2026

@author: julia
"""

def sum_of_digits(digit_string):
    total = 0
    for digit in digit_string:
        total += int(digit)
    return total


def main():
    user_input = input("Enter a sequence of digits with nothing separating them: ")
    result = sum_of_digits(user_input)
    print(f"The total of the digits in the string you entered is {result}")


if __name__ == "__main__":
    main()