#!/usr/bin/python3

# Prompt for the first number
num1 = float(input("Enter the first number: "))

# Prompt for the second number
num2 = float(input("Enter the second number: "))

# Prompt for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the operation using a match-case statement
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:  # Handle division by zero
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        # Handle invalid operation input
        print("Invalid operation. Please choose +, -, *, or /.")
