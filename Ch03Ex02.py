iage= float(input(f'Enter the age of the individual (in months) to classify them: '))
if iage <= 12:
    print(f'This person at {iage:.0f} months is an infant')
elif iage <156:
    print(f'This person at {iage:.0f} months is a child')
elif iage >= 156 and iage < 240:
    print(f'This person at {iage:.0f} months is a teenager')
elif iage >= 240:
    print(f'This person at {iage:.0f} months is an adult')
    
    