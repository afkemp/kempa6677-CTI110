# Avery Kemp
# 2025-11-03
# P4HW2 - Payroll with Totals
# Program calculates regular pay, overtime pay, and gross pay for multiple employees
# and displays total overtime, regular, and gross pay for all employees entered.

"""
PSEUDOCODE
1. Initialize totals (total_ot, total_reg, total_gross, employee_count)
2. Ask for employee name
3. While name is not "Done":
      - Ask for hours worked
      - Ask for pay rate
      - If hours > 40:
            ot_hours = hours - 40
            reg_hours = 40
        else:
            ot_hours = 0
            reg_hours = hours
      - Calculate ot_pay = ot_hours * rate * 1.5
      - Calculate reg_pay = reg_hours * rate
      - Calculate gross = ot_pay + reg_pay
      - Print breakdown
      - Add values to totals
      - Add 1 to employee_count
      - Ask for next employee name
4. When user enters "Done", print totals and number of employees
"""

total_ot = 0
total_reg = 0
total_gross = 0
employee_count = 0

name = input("Enter employee's name or 'Done' to terminate: ")

while name != "Done":
    hours = float(input(f"How many hours did {name} work? "))
    rate = float(input(f"What is {name}'s pay rate? "))

    if hours > 40:
        ot_hours = hours - 40
        reg_hours = 40
    else:
        ot_hours = 0
        reg_hours = hours

    ot_pay = ot_hours * rate * 1.5
    reg_pay = reg_hours * rate
    gross = ot_pay + reg_pay

    print("\nEmployee name:  ", name)
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("-------------------------------------------------------------------------")
    print(f"{hours:<14.1f}{rate:<11.2f}{ot_hours:<11.1f}{ot_pay:<15.2f}${reg_pay:<12.2f}${gross:.2f}\n")

    total_ot += ot_pay
    total_reg += reg_pay
    total_gross += gross
    employee_count += 1

    name = input("Enter employee's name or 'Done' to terminate: ")

print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_ot:.2f}")
print(f"Total amount paid for regular hours: ${total_reg:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
