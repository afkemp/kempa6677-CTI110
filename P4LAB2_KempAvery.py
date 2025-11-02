while True:
    num = int(input("Enter an integer: "))

    if num < 0:
        print("\nThis program does not handle negative numbers.\n")
    else:
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")
        print()

    again = input("Would you like to run the program again? ").strip().lower()
    if again == "yes":
        print()
        continue
    else:
        print("\nExiting program...")
        break
