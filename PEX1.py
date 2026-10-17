# Setting up the first loop that will determine if the user will wish to continue
Keep_Going = "Y"

while Keep_Going == "Y":  # (Outer Most Loop - Run Program - Conditional Loop)

    # Setting the variables I will be referencing throughout the code
    toss = 0.0
    athlete_total = 0.0
    total_dist_avg = 0.0
    Maxtoss = 0.0
    Mintoss = float('inf')   # start very high so first toss replaces it
    TotalMaxtoss = 0.0
    TotalMintoss = float('inf')
    total_all_tosses = 0.0

    # Startup Banner
    print("\n===========================================")
    print("Javelin Competition Toss Program")
    print("===========================================")

    # Requesting user input
    num_athletes = int(input("How many athletes will be competing? "))
    num_toss_per_athlete = int(input("How many tosses do all athletes get? "))

    # Setting up the second loop - number of athletes we will be monitoring
    for athlete in range(1, num_athletes + 1):

        print('\n\n----------------------------------')
        print(f"Athlete {athlete} - Enter Distance")
        print('----------------------------------')

        # Reset per-athlete values
        athlete_total = 0.0
        Maxtoss = 0.0
        Mintoss = float('inf')

        # Inner loop - toss per athlete
        for attempt in range(1, num_toss_per_athlete + 1):

            toss = float(input(f"Javelin Toss {attempt}: What was the distance for the attempt? "))
            athlete_total += toss
            total_all_tosses += toss

            if toss < Mintoss:
                Mintoss = toss

            if toss > Maxtoss:
                Maxtoss = toss

        # Update overall max/min AFTER athlete loop
        if Maxtoss > TotalMaxtoss:
            TotalMaxtoss = Maxtoss

        if Mintoss < TotalMintoss:
            TotalMintoss = Mintoss

        total_dist_avg += (athlete_total / num_toss_per_athlete)

        # Display summary after each athlete
        print("\n==============================================")
        print(f" Javelin Athlete {athlete} Distance Summary")
        print("==============================================")
        print(f"How many javelin tosses were recorded: {num_toss_per_athlete}")
        print(f"What was the average distance for Athlete {athlete}: "
              f"{(athlete_total / num_toss_per_athlete):.2f} meters")
        print(f'The furthest javelin toss for Athlete {athlete} was: {Maxtoss:.2f} meters')
        print(f'The shortest javelin toss for Athlete {athlete} was: {Mintoss:.2f} meters')
        print("==============================================\n")

    # All athletes summary
    print("\n\n***************************************************************************")
    print("\t\t\t\t\tAll Javelin Athlete Distance Summary")
    print("***************************************************************************")

    print(f"Total number of javelin athletes: {num_athletes}")
    print(f"Total number of all javelin tosses (All Athletes combined): "
          f"{num_athletes * num_toss_per_athlete} ")
    print(f"Overall average distance of all Athletes tosses combined: "
          f"{(total_all_tosses / (num_athletes * num_toss_per_athlete)):.2f} meters")
    print(f'The furthest javelin toss for All Athletes was: {TotalMaxtoss:.2f} meters')
    print(f'The shortest javelin toss for All Athletes was: {TotalMintoss:.2f} meters')
    print("***************************************************************************")

    Keep_Going = input("To start over enter 'Y', to exit enter 'N': ")

print("\nThank you for using the Javelin Competition Toss Program, GOODBYE!")