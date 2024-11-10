

# Function to calculate the grade based on the average score
def calculate_grade(average_score):
    if 90 <= average_score <= 100:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'

# Main function
def main():
    # Ask for student's name
    student_name = input("Enter the student's name: ")

    # Ask for number of subjects
    num_subjects = int(input("Enter the number of subjects: "))

    # Initialize a list to store the scores
    scores = []

    # Get the scores for each subject
    for i in range(num_subjects):
        score = float(input(f"Enter score for subject {i+1}: "))
        scores.append(score)

    # Calculate the average score
    average_score = sum(scores) / num_subjects

    # Calculate the grade
    grade = calculate_grade(average_score)

    # Display the results
    print(f"\nStudent Name: {student_name}")
    print(f"Scores: {scores}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Grade: {grade}")

# Run the program
if __name__ == "__main__":
    main()
