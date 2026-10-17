# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:26:32 2026

@author: julia
"""

"""
This program was designed to display a menu of options that will allow the user
to interact with a pre-made list in various ways such as editing the list,
searching the list, and sorting the list
"""

# candies LIST on startup
candies = ['M&Ms','Snickers','Twizzlers','Kit-Kat','Butterfinger','Twix',
'Skittles','Starburst','Smarties','Nerds','SweetTarts','Rolo']

# DISPLAY the program HEADER.
def display_banner():
    print()
    print("=====================================================")
    print("================== Candy Program ====================")
    print("=====================================================")

# DISPLAY the user MENU options.
def display_menu():
    print("\nMenu Options:")
    print("--------------")
    print("1.)  Display the list of candies")
    print("2.)  Display how many candies are in the list")
    print("3.)  Return the index number of a queried candy")
    print("4.)  Search the list for a Candy and display search results")
    print("5.)  Add a candy to the front of the list")
    print("6.)  Add a candy to the end of the list")
    print("7.)  Add a candy to the 2nd to the end of the list")
    print("8.)  Add a candy to the end of the list only if it does not exist in the list")
    print("9.)  Remove a candy from the list")
    print("10.) Sort the candies list (ascending order)")
    print("11.) Sort the candies list (descending order)")
    print("12.) Display the first and last candies in the sorted (ascending) list")
    print("13.) Display the candies in the sorted (ascending order) list A thru L")
    print("14.) Display the candies in the sorted (ascending order) list M thru Z")
    print("15.) Exit/End the program")

# Display all candies in the candies list.
def display_candies():
    print("\n===== Candy List =====")
    for candy in candies:
        print(candy)
    print("======================")

# Display how many candies are available in the list.
def number_of_candies():
    num_candies = len(candies)
    print(f"\nThere are {num_candies} candies in the list.")

# FIND the index number (list position) of a queried candy.
def find_candy_index():
    candy = input("\nEnter the candy to find its index: ")
    candy = candy.title()
    if candy in candies:
        index = candies.index(candy)
        print(f"\nThe Candy '{candy}' is found at index: {index}.")
    else:
        print(f"\n'{candy}' is not found in the list.")

# SEARCH the candies list for for a specific candy.
def search_list():
    candy = input("\nEnter the Name to search: ")
    candy = candy.title()
    if candy in candies:
        print(f"\n{candy} is in the list.")
    else:
        print(f"\n{candy} is not in this list")

# ADD a new candy to the front of the list.
def add_to_front():
    candy = input("\nEnter the Candy to add: ")
    candy = candy.capitalize()
    candies.insert(0, candy)
    print(f"\n'{candy}' was added to the front of the list.")
    display_candies()

# ADD a new candy to the end of the list.
def add_to_end():
    candy = input("\nEnter the Candy to add: ")
    candy = candy.capitalize()
    candies.append(candy)
    print(f"\n'{candy}' was added to the end of the list. ")
    display_candies()

# ADD a new candy second to the last of the list
def second_to_last():
    candy = input("\nEnter the Candy to add: ")
    candy = candy.capitalize()
    candies.insert(len(candies)-1, candy)
    print(f"\n'{candy}' was added second to the last of the list. ")
    display_candies()

# ADD a candy only if it is not already on the list
def does_not_exist():
    new_candy = input('Enter the new Candy to add: ')
    new_candy = new_candy.capitalize()
    if new_candy not in candies:
        candies.append(new_candy)
        print(f"\n'{new_candy}' was added to the end of the list.")
        display_candies()
    else:
        print(f"\n'{new_candy}' already exists in the list.")

# REMOVE a candy from the list.
def remove_entry():
    candy = input("\nEnter the candy to remove: ")
    candy = candy.capitalize()
    if candy in candies:
        candies.remove(candy)
        print(f"\n'{candy}'was removed from the list.")
        display_candies()
    else:
        print(f"\n'{candy}' was not found in the list.")

# SORT the candies list in alphabetical order (ASCENDING order).
def sort_candies():
    candies.sort()
    print("\nThe candies are organized in ascending order.")
    display_candies()

# SORT the candies list in Descending order.
def sort_descending_candies():
    candies.sort(reverse=True)
    print("\nThe candies are organized in descending order.")
    display_candies()

# SORT the list and then gets the first and last candy on the list
def first_and_last_candies():
    candies.sort()
    first = candies[0]
    last = candies[-1]
    print(f'\nThe first candy in the list is {first} and the last candy in the list is {last}.')

# DISPLAY the sorted candies on the list from A through L.
def display_sorted_by_letters_AL():
    candies.sort()
    print("\n===== Candies from A through L =====")
    for candy in candies:
        if candy[0].upper() <= 'L':
            print(candy)
    print("====================================")

# Display the sorted candies on the list from M through Z
def display_sorted_by_letter_MZ():
    candies.sort()
    print("\n===== Candies from M through z =====")
    for candy in candies:
        if candy[0].upper() >= 'M':
            print(candy)
    print("====================================")

# EXIT the program with a goodbye message.
def exit_program():
    print("\nExiting the Candy organizing Program. Goodbye!")

# ASK user to a ENTER a NUMBER from 1-15 in the MENU.
def main():
    display_banner()
    Continue = 'Yes'
    while Continue == 'Yes':
        display_menu()
        choice = input("\nEnter your choice (1-15): ")

        if choice == '1':
            display_candies()
        elif choice == '2':
            number_of_candies()
        elif choice == '3':
            find_candy_index()
        elif choice == '4':
            search_list()
        elif choice == '5':
            add_to_front()
        elif choice == '6':
            add_to_end()
        elif choice == '7':
            second_to_last()
        elif choice == '8':
            does_not_exist()
        elif choice == '9':
            remove_entry()
        elif choice == '10':
            sort_candies()
        elif choice == '11':
            sort_descending_candies()
        elif choice == '12':
            first_and_last_candies()
        elif choice == '13':
            display_sorted_by_letters_AL()
        elif choice == '14':
            display_sorted_by_letter_MZ()
        elif choice == '15':
            exit_program()
            Continue = 'No'
        else:
            print("\nInvalid choice. Please try again.")

main()