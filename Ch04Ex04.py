# -*- coding: utf-8 -*-

# Initialize variables
number = 1.0  # start loop
Min = float('inf')
Max = 0.0
Total = 0.0
counter = 1

# Loop while positive numbers are entered
while number > 0:
    number = float(input(f'Enter a positive number to add and negative number to quit - Number {counter:02}: '))
    
    if number > 0:
        Total += number
        if number < Min:
            Min = number
        if number > Max:
            Max = number
        counter += 1  # increment only when a positive number is entered

# Calculate average
if counter > 1:
    Avg = Total / (counter - 1)
else:
    Avg = 0.0

# Display results
print()
print(f'The minimum of all {counter - 1} numbers is {Min}')
print(f'The maximum of all {counter - 1} numbers is {Max}')
print(f'The average of all {counter - 1} numbers is {Avg:.1f}')
print(f'The total of all {counter - 1} numbers is {Total}')
