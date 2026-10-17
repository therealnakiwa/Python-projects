# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:57:04 2026

@author: julia
"""

# Programming Exercise: Ch08Ex02 - Date Printer - Incomplete
# REPLACE THE ??? WITH THE MISSING CODE TO COMPLETE
# Student Name: Your Name

def main():
    # Local variables
    day = 0
    month_num = 0
    month_name = ''
    date_string = ''
    month_list = ['January', 'February', 'March',
                  'April', 'May', 'June',
                  'July', 'August', 'September',
                  'October', 'November', 'December']

    # Get the date in mm/dd/yyyy format as input from the user.
    date_string = input("Enter the short date format (mm/dd/yyyy) for this famous person's birthday: ")

    # Split date_string.
    date_list = date_string.split("/")

    # Obtain month and day numbers.
    month_num = int(date_list[0])
    day = date_list[1]
    year = date_list[2]

    # Get month_name.
    month_name = month_list[month_num - 1]

    # Create string for long date format.
    long_date = month_name + ' ' + day + ', ' + year

    # Display long date format.
    print(f"The long version of this person's birthday is {long_date}.")

# Call the main function.
if __name__ == '__main__':
    main()