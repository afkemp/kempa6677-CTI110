# Avery Kemp
# 11/27/2025
# P5LAB
# Self-checkout change simulator

import random

def disperse_change(change):
    cents = int(round(change * 100))

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print("Dollars:", dollars)
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies)

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print("Total owed: $", total_owed)

    cash_given = float(input("Enter cash amount: "))
    change = round(cash_given - total_owed, 2)

    print("Change owed: $", change)
    disperse_change(change)

main()
