# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 01:22:46 2026

@author: julia
"""

def main():
    numbers = []

    # Input 20 numbers
    for i in range(1, 21):
        num = float(input(f"Enter number {i} of 20: "))
        numbers.append(num)
    print('-------------------------------')

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print()
    print(f"The lowest number in the list is {lowest:.1f}")
    print(f"The highest number in the list is {highest:.1f}")
    print(f"The average of all the numbers in the list is {average:.1f}")
    print(f"The sum of all the numbers in the list is {total:,.1f}")
    print("-------------------------------")
    print()

    # Sort smallest → largest
    ascending = sorted(numbers)
    print("The numbers in the list sorted from smallest to largest is as follows:")
    for num in ascending:
        print(f"{num:.1f}")

    print("-------------------------------")
    print()

    # Sort largest → smallest
    descending = sorted(numbers, reverse=True)
    print("The numbers in the list sorted from largest to smallest is as follows:")
    for num in descending:
        print(f"{num:.1f}")
    print('-------------------------------')
    print()

if __name__ == "__main__":
    main()