# Avery Kemp
# 10/05/2025
# P2LAB2
# This program stores vehicles and their MPG values in a dictionary.
# The user selects a vehicle, enters miles to drive, and the program
# calculates how many gallons of gas are needed.

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()
print(keys)

choice = input("Enter a vehicle to see its MPG: ")

mpg = vehicles[choice]
print(f"The {choice} gets {mpg} miles per gallon.")

miles = float(input(f"How many miles will you drive the {choice}? "))

gallons = miles / mpg
print(f"{gallons:.2f} gallons are needed to drive the {choice} {miles:.1f} miles.")
