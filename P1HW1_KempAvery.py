# Avery Kemp
# September 25, 2025
# P1HW1_KempAvery
# This program asks the user for numbers and performs exponent, addition, and subtraction calculations.

print("-----Calculating Exponenets----\n")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))


result = base ** exponent

print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

print("-----Addition and Subtraction----\n")

start = int(input("Enter a starting integer: "))
add_val = int(input("Enter an integer to add: "))
sub_val = int(input("Enter an integer to subtract: "))

final_result = start + add_val - sub_val

print(f"\n{start} + {add_val} - {sub_val} is equal to {final_result}")