# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:00:54 2026

@author: julia
"""

# Programming Exercise: Ch08Ex03 - Most Frequent Character - Incomplete
# Student Name: Your Name

def main():
    # Set up local variables
    count = [0] * 26
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    frequent = 0

    # Receive user input.
    user_string = input('Enter a string: ')

    for ch in user_string:
        ch = ch.upper()

        # Determine which letter this character is.
        index = letters.find(ch)

        if index != -1:
            # Increase counting array for this letter.
            count[index] = count[index] + 1

    for i in range(26):
        if count[i] > count[frequent]:
            frequent = i

    print(f"The character that appears most frequently in the string is {letters[frequent]}.")

# Call the main function.
if __name__ == '__main__':
    main()