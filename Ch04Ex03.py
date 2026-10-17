# Ch04Ex03.py

days = int(input("Enter the number of days: "))

print("\nDay:\tPennies\t\tBalance")
print("--------------------------------------------")

pennies = 1
total = 0

for day in range(1, days + 1):
    total += pennies
    
    dollars_today = pennies / 100
    total_dollars = total / 100
    
    print(f"{day:<10}${dollars_today:<10,.2f}${total_dollars:<10,.2f}")
    
    pennies *= 2

print("--------------------------------------------")
print(f"The total salary for {days} days is: ${total/100:,.2f}")
