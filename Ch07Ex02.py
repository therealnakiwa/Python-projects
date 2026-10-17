# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:40:06 2026

@author: julia
"""

def main():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    rainfall = []

    print("***************************")
    print("*** Rainfall Statistics ***")
    print("***************************")

    # Input loop
    for month in months:
        amount = float(input(f"Enter the rainfall for {month}: "))
        rainfall.append(amount)

    total = sum(rainfall)
    average = total / len(rainfall)

    max_rain = max(rainfall)
    min_rain = min(rainfall)

    max_month = months[rainfall.index(max_rain)]
    min_month = months[rainfall.index(min_rain)]
    print('--------------------------------------')
    print()
    print(f"The total rainfall for the year was {total:.1f}")
    print(f"The average rainfall for the year was {average:.1f}")
    print(f"The month with the highest rainfall was {max_month}")
    print(f"The month with the lowest rainfall was {min_month}")

    choice = input("Would you like a detailed summary? (Y/N): ").strip().upper()
    print()

    if choice == "Y":
        print("Rainfall Statistics Detailed Summary")
        print("--------------------------------------")
        
        for i in range(len(months)):
            print(f"The rainfall for {months[i]} was {rainfall[i]:.1f}")

        print("--------------------------------------")
        print(f"The total rainfall for the year was {total:.1f}")
        print(f"The average rainfall for the year was {average:.1f}")
        print(f"The month with the highest rainfall was {max_month}")
        print(f"The month with the lowest rainfall was {min_month}")
        print()
        print("Have a good day!")
        print("Program stopped...")
    else:
        print("Have a good day!")
        print("Program stopped...")


if __name__ == "__main__":
    main()