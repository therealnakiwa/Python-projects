# -*- coding: utf-8 -*-
# Program: email per employee counter
# Description:
#   This program analyzes how many emails are sent per employee
#   in an officeover several days.
#   It uses nested loops and decision structures to calculate:
#       - Subtotals for each employee (inner loop)
#       - Totals for all employees (middle loop)
#   The program:
#       - Outer loop: run the whole Analyzer again or exit
#       - Middle loop: loop through each employee
#       - Inner loop: loop through each day for that employee
#   It calculates Subtotal count, total, average, maximum, minimum
#         for each employee (inner loop)
#       - Combined count, total, average, maximum, minimum
#         for all employees (middle loop)
#   The theme "emails Sent per Employee" appears in banners,
#   prompts, variables, and comments.

print("=======================================================")
print("        Officeemail Productivity Analyzer")
print("        \"emails Sent per Employee\" - Exam 1")
print("=======================================================")
print("Welcome to the Officeemail Productivity Analyzer.")
print("This tool will help you review how many emails")
print("your employees send over one or more workdays.")
print("-------------------------------------------------------\n")


isrunning = False   # Controls entire program start/restart

while isrunning == False:
    # New analysis session banner
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("      New email Productivity Analysis Session")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    #  number of employees/middleloop
    employees_valid = False
    while employees_valid == False:
        emp_text = input("Enter number of employees (1 or more): \n")
        # If the input is not a valid integer, the program will crash
        if emp_text != "":
            employees = int(emp_text)
            if employees >= 1:
                employees_valid = True
            else:
                print("enter at least 1 employee.\n")
        else:
            print("Please do not leave this blank.\n")
    numofwork = employees
    ote = 0        # Total emails 
    totale = 0       # Total number of day entries
    ome = 0          # Maximum daily emails of any employee
    officeminemails = 0          # Minimum daily emails of any employee
    ohd = False        # Flag to know if any data exists

    #middle loop to check every employee
    id = 1
    while id <= numofwork:
        print("-------------------------------------------------------")
        print(" email Productivity for each employee:", id)
        print("-------------------------------------------------------")

        # NUMBER OF DAYS FOR THIS EMPLOYEE 
        dv = False
        while dv == False:
            days_text = input("Enter number of days tracked for this employee: \n")
            if days_text != "":
                edays = int(days_text)
                if edays >= 1:
                    dv = True
                else:
                    print("Number of days must be at least 1.\n")
            else:
                print("Please do not leave this blank.\n")


        # INNER LOOP: emails per day for this employee 
        # Inner loop subtotal variables for this employee
        ete = 0      #  Total
        eoc = 0       #  Number of loops
        omme = 0        #  Maximum
        minnie = 0        #  Minimum
        hasdata = False      # To handle first day's data

        day = 1
        while day <= edays:
            print("Day", day, "- Employee", id)
            txtemails = input("Enter number of emails sent on this day (whole number): \n")

            if txtemails != "":
                etdy = int(txtemails)

                # Update inner loop count and total
                eoc = eoc + 1
                ete = ete + etdy

                # For first day, set max and min
                if hasdata == False:
                    omme = etdy
                    minnie = etdy
                    hasdata = True
                else:
                    # Update maximum emails manually
                    if etdy > omme:
                        omme = etdy
                    # Update minimum emails manually
                    if etdy < minnie:
                        minnie = etdy

                # Move to next day
                day = day + 1
            else:
                print("Please do not leave this blank.\n")
        # Calculate inner loop average for this employee using floating point division
        if eoc > 0:
            eae = ete / float(eoc)
        else:
            eae = 0.0

        # --------- Display inner loop subtotal results for this employee ---------
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(" email subtotals for employee/s", id)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(f"Number of days recorded: {eoc}")
        print(f"Total emails sent: {ete}")
        print(f"Average emails per day: {eae:.2f} ")
        print(f"Maximum emails in a single day: {omme}" )
        print(f"Minimum emails in a single day: {minnie}")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print()

        # Update office-wide (middleloop} totals
        if eoc > 0:
            totale = totale + eoc
            ote = ote + ete

            if ohd == False:
                ome = omme
                officeminemails = minnie
                ohd = True
            else:
                # Update overall maximum emails per day
                if omme > ome:
                    ome = omme
                # Update overall minimum emails per day
                if minnie < officeminemails:
                    officeminemails = minnie

        # Move to next employee
        id = id + 1
    # Calculate office-wide averages (middle loop average) 
    if totale > 0:
        oae = ote / float(totale)
    else:
        oae = 0.0

    # Display combined results for all employees
    print("#######################################################")
    print(" Combined email Productivity results - ALL EMPLOYEES")
    print("#######################################################")
    print(f"Total day entries (all employees):{totale}")
    print(f"Total emails sent (all employees):{ote}")
    print(f"Average emails per day (office-wide):{oae:.2f}")
    print(f"Highest emails in a single day (office): {ome}")
    print(f"Lowest emails in a single day (office):  {officeminemails}")
    print("#######################################################\n")

    #desicion to continue or end
    print("Press any key to start another email Productivity Analysis session")
    print("2 - Exit the Officeemail Productivity Analyzer")
    restart = input("Enter any key to start again, or 2 to exit: \n")

    if restart == "2":
            print("Thank you for using the Office email Productivity Analyzer.")
            print("Shutting down, Goodbye!")
            isrunning = True
    else:
        print("Restarting email Productivity Analysis session\n")
    