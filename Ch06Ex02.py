# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:33 2026

@author: julia
"""

def main():
    # 1. Initialize an accumulator variable to 0.0
    total = 0.0

    # 2. Open the file 'numbers.txt' for reading
    # The file is preloaded in the tester, so we just use the name
    try:
        infile = open('numbers.txt', 'r')

        # 3. Use a for-loop to read each line in the file
        for line in infile:
            # Convert the line to a float and add it to the total
            number = float(line)
            total += number

        # 4. Close the file
        infile.close()

        # 5. Display the result exactly as shown in the expected output
        # :,.1f adds the comma and one decimal place
        print(f"The total of all the numbers in the file is {total:,.1f}")

    except FileNotFoundError:
        print("The file numbers.txt was not found.")

if __name__ == "__main__":
    main()
