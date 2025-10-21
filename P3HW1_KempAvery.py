# P3HW1 - Debugging and Lists
# Name: Kemp, Avery
# Date: 2025-10-26
# Ask for six module grades, store them in a list, then show
# lowest, highest, sum, average, and the letter grade.

grades = [float(input(f"Enter grade for Module {i}: ")) for i in range(1, 7)]

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("\n------------Results------------")
print(f"Lowest Grade:  {lowest:.1f}")
print(f"Highest Grade: {highest:.1f}")
print(f"Sum of Grades: {total:.1f}")
print(f"Average:       {average:.2f}")
print("--------------------------------\n")

if average >= 90:
    letter = "A"
elif average >= 80:
    letter = "B"
elif average >= 70:
    letter = "C"
elif average >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Your grade is: {letter}")
