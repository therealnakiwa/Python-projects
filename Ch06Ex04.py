def main():
    try:
        infile = open('steps.txt', 'r')

        # Use a loop from 1 to 12 to represent the months
        for month_num in range(1, 13):
            month_name = ""
            num_days = 0

            # Logic to assign month name and days without using a list
            if month_num == 1:
                month_name, num_days = "January", 31
            elif month_num == 2:
                month_name, num_days = "February", 28
            elif month_num == 3:
                month_name, num_days = "March", 31
            elif month_num == 4:
                month_name, num_days = "April", 30
            elif month_num == 5:
                month_name, num_days = "May", 31
            elif month_num == 6:
                month_name, num_days = "June", 30
            elif month_num == 7:
                month_name, num_days = "July", 31
            elif month_num == 8:
                month_name, num_days = "August", 31
            elif month_num == 9:
                month_name, num_days = "September", 30
            elif month_num == 10:
                month_name, num_days = "October", 31
            elif month_num == 11:
                month_name, num_days = "November", 30
            elif month_num == 12:
                month_name, num_days = "December", 31

            month_total = 0
            # Read exactly the number of lines for this month
            for day in range(num_days):
                line = infile.readline()
                if line:
                    month_total += int(line)

            average = month_total / num_days
            display_results(month_name, average)

        infile.close()

    except FileNotFoundError:
        print("The file steps.txt was not found.")

def display_results(month, avg):
    # Formatting with comma and one decimal place as required
    print(f"The average steps taken in {month} was {avg:,.1f}")

if __name__ == "__main__":
    main()
