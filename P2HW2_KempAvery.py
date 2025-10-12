# Avery Kemp
# 2025-10-11
# P2HW2 – Lists and Grade Stats
# Program asks for six module grades, stores them in a list, and displays
# the lowest, highest, sum, and average in formatted output.

m1 = float(input("Enter grade for Module 1: "))
m2 = float(input("Enter grade for Module 2: "))
m3 = float(input("Enter grade for Module 3: "))
m4 = float(input("Enter grade for Module 4: "))
m5 = float(input("Enter grade for Module 5: "))
m6 = float(input("Enter grade for Module 6: "))

module_grades = [m1, m2, m3, m4, m5, m6]

lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

print("\n------------Results------------")
label_w = 18
val_w = 8
print(f'{"Lowest Grade:":<{label_w}}{lowest:>{val_w}.1f}')
print(f'{"Highest Grade:":<{label_w}}{highest:>{val_w}.1f}')
print(f'{"Sum of Grades:":<{label_w}}{total:>{val_w}.1f}')
print(f'{"Average:":<{label_w}}{average:>{val_w}.2f}')
print("-" * 32)
