

# Function to generate the Fibonacci sequence
def fibonacci_sequence(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Main function
def main():
    # Get the number of terms from the user
    try:
        n = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate the Fibonacci sequence
        sequence = fibonacci_sequence(n)
        
        # Print the sequence in a single line, separated by commas
        print(", ".join(map(str, sequence)))
        
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main()

