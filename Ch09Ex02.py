# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:03:18 2026

@author: julia
"""



def main():
    # Set up empty dictionary
    counter = {}

    # Get the name of the input file.
    input_name = input('Enter the name of the input file: ')
    lower_words = []

    # Get input text
    with open(input_name, 'r') as input_file:
        text = input_file.read()
    
    # Split the text into words.
    words = text.split()
    
    for word in words:
            word = word.lower()
            lower_words.append(word)
    
    
    # Add each unique word to dictionary with a counter of 0
    unique_words = lower_words
    unique_words = set(unique_words)
    unique_words = sorted(unique_words)
    
    for word in unique_words:
        counter[word] = 0

    # For each word in the text increase its counter in the dictionary
    for item in lower_words:
        counter[item] += 1

    # Display results
    print(f'{"Word":15}\t{"Occurrences":15}')
    print('----------------------------------------------')

    for k, v in counter.items():
        print(f'{k:15}{v:<15}')

# Call the main function.
if __name__ == '__main__':
    main()