# P3HW2_Salary_KempAvery.py
# Your Name
# Date
# P3HW2 – Salary Calculator
# This program asks for an employee's name, hours worked, and pay rate.
# It computes overtime (over 40 hours) at 1.5x, regular pay, and gross pay,
# then prints a nicely formatted pay summary.

"""
PSEUDOCODE
----------
1) Prompt for employee name -> name
2) Prompt for hours worked -> hours (float)
3) Prompt for pay rate -> rate (float)

4) If hours > 40:
       reg_hours = 40
       ot_hours = hours - 40
   Else:
       reg_hours = hours
       ot_hours = 0

5) reg_pay = reg_hours * rate
6) ot_pay  = ot_hours  * rate * 1.5
7) gross   = reg_pay + ot_pay

8) Print a header line
9) Print "Employee name: " and the name
10) Print column headers with alignment
11) Print one row with hours, rate, overtime hours, overtime pay,
    regular pay, and gross pay, aligned and with 2 decimals
"""

name  = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate  = float(input("Enter employee's pay rate: "))

if hours > 40:
    reg_hours = 40
    ot_hours = hours - 40
else:
    reg_hours = hours
    ot_hours = 0.0

reg_pay = reg_hours * rate
ot_pay  = ot_hours * rate * 1.5
gross   = reg_pay + ot_pay

print("-" * 60)
print(f"Employee name:  {name}\n")

print(f'{"Hours Worked":<14}{"Pay Rate":<10}{"OverTime":<10}'
      f'{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<12}')
print("-" * 90)

print(f"{hours:<14.1f}{rate:<10.2f}{ot_hours:<10.1f}"
      f"${ot_pay:<14.2f}${reg_pay:<14.2f}${gross:<12.2f}")
