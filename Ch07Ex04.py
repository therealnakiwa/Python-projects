# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:40:50 2026

@author: julia
"""

def main():
    # 1. Initialize an empty list to store the names
    popular_names = []

    try:
        # 2. Read the contents of the file into the list
        # We use a 'for in' loop here to satisfy the repetitive structure requirement
        with open('popular_names.txt', 'r') as file:
            for line in file:
                # Strip newline characters and add to the list
                popular_names.append(line.strip())

        # 3. Get user input
        search_name = input("Enter a name to check if it was a popular name: ")

        # 4. Search the list for the name
        # Using a loop to check for the name (satisfying the 'for in' requirement)
        found = False
        for name in popular_names:
            if name.lower() == search_name.lower():
                found = True
                break

        # 5. Display the result using f-strings
        if found:
            print(f"{search_name} was a popular name between 2000 and 2009.")
        else:
            print(f"{search_name} was not a popular name between 2000 and 2009.")

    except FileNotFoundError:
        print("Error: The file 'popular_names.txt' was not found.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
