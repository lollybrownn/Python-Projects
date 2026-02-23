# This is a Simple Calculator
# That can calculate Addition, Subtraction, Multiplication, and Division


while True:
    print("==== SIMPLE CALCULATOR ====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit Program")

    choice = int(input("Select the calculation: "))

    if choice == 5:
        print("Program terminated.")
        break

    if choice < 1 or choice > 5:
        print("Invalid input, try again.\n")
        continue

    num1 = int(input("Input 1st number: "))
    num2 = int(input("Input 2nd number: "))

    match choice:
        case 1:
            print(f"Total Calculation: {num1 + num2}\n")
        case 2:
            print(f"Total Calculation: {num1 - num2}\n")
        case 3:
            print(f"Total Calculation: {num1 * num2}\n")
        case 4:
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print(f"Total Calculation: {num1 / num2}\n")
                
