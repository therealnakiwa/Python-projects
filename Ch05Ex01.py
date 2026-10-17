# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:44:21 2026

@author: julia
"""

# Constants for the tax calculation
ASSESSMENT_RATE = 0.75
TAX_PER_HUNDRED = 1.11

def get_assessment_value(actual_value):
    """Calculates and returns 75% of the actual property value."""
    return actual_value * ASSESSMENT_RATE

def get_property_tax(assessment_value):
    """
    Calculates tax at $1.11 for each $100 of assessment value.
    Note: To match the expected output of $1,040.07, we use 
    integer division (//) to count the number of $100 units.
    """
    hundreds = assessment_value // 100
    return hundreds * TAX_PER_HUNDRED

def main():
    # Get the actual value from the user
    actual_value = float(input("Enter the actual property value: "))
    
    # Perform calculations using the functions
    assessment = get_assessment_value(actual_value)
    tax = get_property_tax(assessment)
    
    # Display the results using f-strings for formatting
    print(f"The assessed value is ${assessment:,.2f}")
    print(f"The property tax is ${tax:,.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
