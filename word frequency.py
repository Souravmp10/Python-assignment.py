

import string

# Function to count word frequencies
def count_word_frequencies(text):
    # Convert text to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store word frequencies
    word_frequency = {}
    
    # Count frequency of each word
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
            
    return word_frequency

# Main function
def main():
    # Get the paragraph input from the user
    text = input("Enter a paragraph of text: ")
    
    # Get the word frequencies
    word_frequencies = count_word_frequencies(text)
    
    # Print each word and its frequency
    print("\nWord frequencies:")
    for word, frequency in word_frequencies.items():
        print(f"{word}: {frequency}")

# Run the program
if __name__ == "__main__":
    main()

