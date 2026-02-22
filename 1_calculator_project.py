# This is a Simple Calculator
# That can calculate Addition, Subtraction, Multiplication, and Division

print("==== SIMPLE CALCULATOR ====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Select the calculation: "))

num1 = int(input("\nInput 1st number: "))
num2 = int(input("Input 2nd number: "))

match choice:
    case 1:
        total = num1 + num2
    case 2:
        total = num1 - num2
    case 3:
        total = num1 * num2
    case 4:
        total = num1 / num2
    case _:
        total = "\nInvalid input, try again"

print(f"\nTotal Calculation: {total}")
