

# Simple Calculator Program

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation."

# Take input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

# Display the available operations
print("Select an operation:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")

# Take the operation input from the user
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation and display the result
result = calculate(num1, num2, operation)
print(f"The result of {num1} {operation} {num2} is: {result}")
