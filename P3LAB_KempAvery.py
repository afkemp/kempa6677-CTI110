# Kemp, Avery
# Description:
#   Prompt the user for a money amount (float with two decimals) and display the
#   most efficient combination of Dollars, Quarters, Dimes, Nickels, and Pennies.
#   - Use floor division (//) and subtraction for logic.
#   - Omit any denomination with a count of 0.
#   - Use singular/plural correctly (e.g., "Penny" vs "Pennies").
#   - Match sample I/O formatting (prompt + Title-Case coin names).

amount = float(input("Enter the amount of money as a float: $"))

cents = int(round(amount * 100))

dollars = cents // 100
cents -= dollars * 100

quarters = cents // 25
cents -= quarters * 25

dimes = cents // 10
cents -= dimes * 10

nickels = cents // 5
cents -= nickels * 5

pennies = cents

def print_line(count, singular, plural):
    if count == 1:
        print(f"1 {singular}")
    elif count > 1:
        print(f"{count} {plural}")

# Output
if dollars == quarters == dimes == nickels == pennies == 0:
    print("No change")
else:
    print_line(dollars, "Dollar", "Dollars")
    print_line(quarters, "Quarter", "Quarters")
    print_line(dimes, "Dime", "Dimes")
    print_line(nickels, "Nickel", "Nickels")
    print_line(pennies, "Penny", "Pennies")
