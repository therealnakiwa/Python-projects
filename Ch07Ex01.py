# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:14:38 2026

@author: julia
"""

def main():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    sales = []

    print("Welcome to the Daily Sales Accumulator")
    print("ENTER THE SALES FOR THE WEEK")
    print("------------------------------------------")

    # Collect sales for each day
    for day in days:
        amount = float(input(f"Enter the sales for {day}: "))
        sales.append(amount)

    total_sales = sum(sales)

    print("------------------------------------------")
    print(f"Total sales for the week was ${total_sales:,.2f}")
    print()

    choice = input("Would you like to view a detailed summary? (N/Y) : ").strip().upper()
    print()

    if choice == "Y":
        print("DETAILED WEEK SUMMARY")
        print("------------------------------------------")
        for i in range(len(days)):
            print(f"{days[i]}'s sales were ${sales[i]:,.2f}")
        print("------------------------------------------")
        print(f"Total sales for the week was ${total_sales:,.2f}")
        print()
        print("Thank you for using Daily Sales Accumulator")
        print("Program ended....")
    else:
        print("Thank you for using Daily Sales Accumulator")
        print("Program ended....")


# Run the program
if __name__ == "__main__":
    main()