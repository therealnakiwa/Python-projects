# Constants
SQ_FT_PER_GALLON = 90
HOURS_PER_GALLON = 7
LABOR_CHARGE_PER_HOUR = 45.00

def main():
    # Header - Using asterisks as requested
    print("***********************")
    print("* PAINT JOB ESTIMATOR *")
    print("***********************")

    # Input
    sq_ft = float(input("Enter wall space in square feet: "))
    paint_price = float(input("Enter paint price per gallon: "))

    # Calculations (Manual Ceiling Logic)
    # Get the base number of gallons using integer division
    gallons_needed = int(sq_ft // SQ_FT_PER_GALLON)
    
    # If there is any remainder, we need to buy one more full gallon
    if sq_ft % SQ_FT_PER_GALLON > 0:
        gallons_needed += 1

    # Total calculations based on the rounded-up gallons
    hours_needed = gallons_needed * HOURS_PER_GALLON
    paint_cost = gallons_needed * paint_price
    labor_cost = hours_needed * LABOR_CHARGE_PER_HOUR
    total_cost = paint_cost + labor_cost

    # Display results
    display_results(gallons_needed, hours_needed, paint_cost, labor_cost, total_cost)

def display_results(gallons, hours, p_cost, l_cost, total):
    # Wording matches the image precisely
    print(f"\nThe total gallons of paint needed for the job is {gallons}")
    print(f"The total of hours of labor required for the job is {hours}")
    print(f"The total paint cost for the job is ${p_cost:,.2f}")
    print(f"The total labor cost for the job is ${l_cost:,.2f}")
    
    # Separator - Using asterisks
    print("**********************************************************")
    print(f"Total estimate for the paint job totals to ${total:,.2f}")

if __name__ == "__main__":
    main()