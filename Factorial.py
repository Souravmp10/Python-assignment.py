

# Function to calculate factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial_recursive(n - 1)  # Recursive case

# Function to calculate factorial using iteration
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from the user
try:
    number = int(input("Enter a positive integer: "))
    if number < 0:
        print("Please enter a positive integer.")
    else:
        # Compute factorial using both methods
        recursive_result = factorial_recursive(number)
        iterative_result = factorial_iterative(number)
        
        # Print the results
        print(f"Factorial of {number} (using recursion): {recursive_result}")
        print(f"Factorial of {number} (using iteration): {iterative_result}")
        
except ValueError:
    print("Invalid input! Please enter a validinteger")


