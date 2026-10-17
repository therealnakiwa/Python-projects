# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:59:44 2026

@author: julia
"""


def main():
    # Get name of input file.
    input_name = input('Enter the name of the input file: ')
    lower_words = []
    
    # Open the input file and read the text.
    with open(input_name, 'r') as input_file:
        text = input_file.read()
        words = text.split()
        
        for word in words:
            word = word.lower()
            lower_words.append(word)

        # Create set of unique words.
        unique_words = set()
        unique_words = set(lower_words)
        unique_words = sorted(unique_words)
        

        # Print the results.
        print('These are the unique words in the text:')
        for word in unique_words:
            print(word)

# Call the main function.
if __name__ == '__main__':
    main()