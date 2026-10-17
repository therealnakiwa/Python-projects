# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:39:49 2026

@author: julia
"""

def main():
    # Open the file in read mode ('r')
    # Make sure 'numbers.txt' is in the same folder as your script
    file = open('numbers.txt', 'r')

    # Use a loop to read the file line by line
    for line in file:
        # .strip() removes the hidden newline character (\n) at the end of each line
        number = line.strip()
        print(number)

    # Always close the file when you are done
    file.close()

# Call the main function to run the program
if __name__ == "__main__":
    main()
