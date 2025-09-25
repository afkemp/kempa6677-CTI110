# Avery Kemp
# September 25, 2025
# P1HW2_KempAvery
# This program asks the user for a budget and trip expenses, then calculates remaining balance.

# Pseudocode:
# 1. Ask user to enter starting budget
# 2. Ask user to enter travel destination
# 3. Ask user for amount they will spend on gas
# 4. Ask user for amount they will spend on accommodation
# 5. Ask user for amount they will spend on food
# 6. Add all expenses together
# 7. Subtract expenses from budget to get remaining balance
# 8. Display travel destination, budget, expenses, and remaining balance

print("This program calculates and displays travel expenses\n")

# Collect user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate expenses and balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print("---------------------------------------")
print(f"Remaining Balance: ${remaining_balance:.2f}")


