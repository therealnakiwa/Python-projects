co1 = input('Enter the first primary color (in lower case letters): ')
co2 = input('Enter the second primary color (in lower case letters): ')

# First, validate the colors
if co1 != 'red' and co1 != 'blue' and co1 != 'yellow':
    print("Error: The first color you entered is invalid.")
elif co2 != 'red' and co2 != 'blue' and co2 != 'yellow':
    print("Error: The second color you entered is invalid.")
else:
    # Both colors are valid; now figure out the result
    if (co1 == 'red' and co2 == 'blue') or (co1 == 'blue' and co2 == 'red'):
        print('purple')
    elif (co1 == 'red' and co2 == 'yellow') or (co1 == 'yellow' and co2 == 'red'):
        print('orange')
    elif (co1 == 'blue' and co2 == 'yellow') or (co1 == 'yellow' and co2 == 'blue'):
        print('green')
    else:
        # Same color twice, e.g., red + red
        print(co1)

