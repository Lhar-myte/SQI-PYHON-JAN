def addition(first_num, second_num):
    return f"{first_num} + {second_num} = {round(first_num + second_num, 2)}"

def subtraction(num1, num2):
    return f"{num1} - {num2} = {round(num1 - num2, 2)}"

def multiplication(num1, num2):
    return f"{num1} X {num2} = {round(num1 * num2, 2)}"

def division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return f"{num1} / {num2} = {round(num1 / num2, 2)}"

menu = """
1. Addition.
2. Subtraction
3. Multiplication
4. Division
5. Quit
"""

while True:
    print(menu)

    choice = input("Choose an option from the menu above: ").strip()

    if choice == "5":
        print("Program terminated")
        break

    if choice not in "1234":
        print("invalid choice, choose from the menu")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print(addition(num1, num2))
    elif choice == "2":
        print(subtraction(num1, num2))
    elif choice == "3":
        print(multiplication(num1, num2))
    elif choice == "4":
        print(division(num1, num2))
