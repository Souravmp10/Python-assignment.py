

# Function to accept a dictionary from the user
def get_user_input():
    user_input = input("Enter a dictionary (e.g. {'key1': 'value1', 'key2': 'value2'}): ")
    # Converting the string input into an actual dictionary
    try:
        dictionary = eval(user_input)
        if not isinstance(dictionary, dict):
            print("That's not a valid dictionary.")
            return None
        return dictionary
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to sort the dictionary by keys
def sort_dict_by_keys(dictionary):
    # Sorting the dictionary by its keys and returning the sorted dictionary
    return dict(sorted(dictionary.items()))

# Main function
def main():
    # Get dictionary input from user
    dictionary = get_user_input()
    if dictionary is not None:
        # Sort the dic       sorted_dict = sort_dict_by_keys(dictionary)
        # Print the sorted dictionary
        print("Sorted Dictionary by Keys:", sorted_dict)

# Run the program
if __name__ == "__main__":
    main()
