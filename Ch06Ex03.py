# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:26:09 2026

@author: julia
"""

def main():
    # 1. Initialize accumulator and counter
    total = 0.0
    count = 0

    # 2. Open the file 'numbers.txt' for reading
    try:
        infile = open('numbers.txt', 'r')

        # 3. Use a for-loop to read each line
        for line in infile:
            # Convert the line to a number and add to total
            value = float(line)
            total += value
            
            # Increment count for each number read
            count += 1

        # 4. Close the file
        infile.close()

        # 5. Calculate average and display result
        # Check to avoid division by zero if the file is empty
        if count > 0:
            average = total / count
            # .1f ensures the result is 454.6 (one decimal place)
            print(f"The average of all the numbers in the file is {average:.1f}")
        else:
            print("No numbers found in the file.")

    except FileNotFoundError:
        print("The file numbers.txt was not found.")

# Call the main function
if __name__ == "__main__":
    main()
