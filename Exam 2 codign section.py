# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:03:59 2026

@author: julia
"""

# This progeam is a show watchlist manager, it allows users to manage 
# watchlists by being able to add, remove, and sort shows according to the 
# user, changing when they register that they have watched the show

#global list

watchlist = []
shows_watched = []
# display menu function

def display_menu():
    print("\n <<<<<<< Watchlist Manager >>>>>>>")
    print('1. View Watchlist')
    print('2. Add Show to Watchlist')
    print('3. Remove show from Watchlist')
    print('4. Search Show')
    print('5. Mark as watched')
    print('6. View watched shows')
    print('0. Leave the program')

# function to view watclist
def view_watchlist():
    if len(watchlist) == 0:
        print('The watchlist is empty, please add shows')
    else:
        print('\n Your Watchlist')
        for show in watchlist:
            print(f'- {show}')
            
#function to add shows

def add_shows():
    show = input('Enter show to add to Watchlist: ')
    if show in watchlist or shows_watched:
        print('You have already put this show in the list, please put a differnet one')
    else:
        watchlist.append(show)
        print(f'{show} was added to watchlist ')
    
#function to remove shows
def remove_show():
    show = input('Enter show name to remove: ')
    if show in watchlist:
        watchlist.remove(show)
        print(f'{show} was removed from the Watchlist'  )
    else: 
        print("Show was not found in watchlist ")
        
#function to find shows in watchlist
def search_show():
    show = input('Enter show name to search: ')
    if show in watchlist():
        print(f'{show} is in Watchlist')
    else:
        print('Show is not in Watchlist')
    
#Function to mark shows
def mark_watched():
    show = input("Enter show watched: ")
    if show in watchlist:
        watchlist.remove(show)
        shows_watched.append(show)
        print('Congrats for finishing a new show')
    else: 
        print('show not found')
# function to sort watchlist
def sort_watchlist():
    watchlist.sort()
    print('Watchlist has been sorted alphabetlically')

#view watched shows
def view_watched_shows():
    if len(shows_watched) == 0:
        print('you havent watched any shows yet')
    else:
        print('\n Your Shows watched')
        for show in shows_watched:
            print(f'- {show}')

# main function
def main():
    choice = -1
    while choice != 0:
        display_menu()
        
        try:
            choice = int(input('Enter your choice: '))
        except:
            print('Invalid input, enter a number')
            
            
        if choice == 1:
            view_watchlist()
        elif choice == 2:
            add_shows()
        elif choice == 3:
            remove_show()
        elif choice == 4:
            search_show()
        elif choice == 5:
            mark_watched()
        elif choice == 6:
            view_watched_shows()
        elif choice == 0:
            print('Thank you for using program, goodbye!!!')
        else: 
            print('invalid choice, try again')
            
# run program
main()
            
            
        
        

         
