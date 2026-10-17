# Ch04Ex02.py

years = int(input("Enter the number of rainfall years to record: "))
print()

total_rainfall = 0.0
total_months = years * 12

for year in range(1, years + 1):

    if year > 1:
        print()

    print("**************")
    print(f"*** Year {year} ***")
    print("**************")

    for month in range(1, 13):
        amount = float(input(
            f"Enter the rainfall amount for (year {year}/month {month}): "
        ))
        total_rainfall += amount

average_rainfall = total_rainfall / total_months

print()
print(f"For {total_months} months, there was a total rainfall of "
      f"{total_rainfall:.1f} inches with an average monthly rainfall of "
      f"{average_rainfall:.1f} inches.")
