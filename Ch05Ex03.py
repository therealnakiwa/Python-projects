# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:03:59 2026

@author: julia
"""

def main():
    # Input
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    num3 = float(input("Enter number 3: "))

    # Logic: Check if they are all the same first
    if check_same(num1, num2, num3):
        print("\nAll numbers are the same")
    else:
        # Calculate values using return functions
        minimum = get_min(num1, num2, num3)
        maximum = get_max(num1, num2, num3)
        total = get_total(num1, num2, num3)
        average = get_avg(total)
        
        # Display results using a void function
        display_results(minimum, maximum, average, total)

# Function (return): Returns True if all three are equal
def check_same(n1, n2, n3):
    if n1 == n2 and n2 == n3:
        return True
    else:
        return False

# Function (return): Manual logic to find the minimum
def get_min(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3

# Function (return): Manual logic to find the maximum
def get_max(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

# Function (return): Calculate total
def get_total(n1, n2, n3):
    return n1 + n2 + n3

# Function (return): Calculate average
def get_avg(total_val):
    return total_val / 3

# Function (void): Displays the formatted output
def display_results(low, high, avg, total):
    print(f"\nThe minimum number is: {low:.1f}")
    print(f"The maximum number is: {high:.1f}")
    print(f"The average of the numbers is: {avg:.1f}")
    print(f"The total of the numbers is: {total:.1f}")

if __name__ == "__main__":
    main()