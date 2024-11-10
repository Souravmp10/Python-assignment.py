

# Function to check if a string has all unique characters
def has_unique_characters(input_string):
    # Convert the string to lowercase and remove spaces
    input_string = input_string.lower().replace(" ", "")
    
    # Use a set to track characters we've already seen
    seen_characters = set()

    # Iterate over each character in the string
    for char in input_string:
        if char in seen_characters:
            # If the character is already in the set, return False
            return False
        seen_characters.add(char)
    
    # If no characters are repeated, return True
    return True

# Main function
def main():
    # Take input string from the user
    input_string = input("Enter a string: ")
    
    # Check if the string has all unique characters
    result = has_unique_characters(input_string)
    
    # Print the result (True or False)
    print(result)

# Run the program
if __name__ == "__main__":
    main()

