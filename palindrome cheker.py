

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_str = ''.join(s.split()).lower()
    
    # Check if the string is equal to its reverse
    if cleaned_str == cleaned_str[::-1]:
        print(True)
    else:
        print(False)

# Example usage
is_palindrome("A man a plan a canal Panama")  # This should print True
is_palindrome("hello")  # This should print False




