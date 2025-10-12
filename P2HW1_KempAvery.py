# Avery Kemp
# 2025-10-11
# P2HW1 – Travel Expenses (Formatting)
# Enhances P1HW2 by formatting output with aligned columns and currency.

print("This program calculates and displays travel expenses\n")

budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")

fuel = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much will you need for accomodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

total_expenses = fuel + hotel + food
remaining = budget - total_expenses

label_w = 15
value_w = 15

print("\n------------Travel Expenses------------")
print(f'{"Location:":<{label_w}}{destination:>{value_w}}')
print(f'{"Initial Budget:":<{label_w}}${budget:>{value_w-1},.2f}')
print(f'{"Fuel:":<{label_w}}${fuel:>{value_w-1},.2f}')
print(f'{"Accomodation:":<{label_w}}${hotel:>{value_w-1},.2f}')
print(f'{"Food:":<{label_w}}${food:>{value_w-1},.2f}')
print("-" * (label_w + value_w))

print(f"\nRemaining Balance:  ${remaining:,.2f}")
