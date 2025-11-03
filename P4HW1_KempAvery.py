# Avery Kemp
# 2025-11-03
# P4HW1 - Score List & Grade
# Build on earlier assignment: collect N scores with validation,
# drop the lowest score, show modified list, average, and letter grade.

"""
PSEUDOCODE
1) Ask the user how many scores they want to enter -> n
2) Make an empty list called scores
3) For i from 1 to n:
      prompt = "Enter score #i: "
      read value -> s (as float)
      while s < 0 or s > 100:
          print "INVALID Score entered!!!!"
          print "Score should be between 0 and 100"
          prompt again -> "Enter score #i again: "
          read s
      append s to scores
4) lowest = min(scores)
5) modified = copy of scores; remove ONE instance of lowest from modified
6) average = sum(modified) / length(modified)
7) Determine letter grade from average:
      90-100: A, 80-89.99: B, 70-79.99: C, 60-69.99: D, else: F
8) Print results formatted like the example
"""

count = int(input("How many scores do you want to enter? "))

scores = []
for i in range(1, count + 1):
    s = float(input(f"Enter score #{i}: "))
    while s < 0 or s > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        s = float(input(f"Enter score #{i} again: "))
    scores.append(s)

lowest = min(scores)

modified = list(scores)    
modified.remove(lowest)

average = sum(modified) / len(modified)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n-------------Results------------")
print(f"Lowest Score   : {lowest:.1f}")
print(f"Modified List  : {modified}")
print(f"Scores Average : {average:.2f}")
print(f"Grade          : {grade}")
print("--------------------------------")
