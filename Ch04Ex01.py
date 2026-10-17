tbugs = 0
for day in range(1,8):
    btoday= int(input(f"Enter the number of bugs collected on day {day}: "))
    tbugs += btoday
    
print(f"You collected a total of {tbugs} bugs.")