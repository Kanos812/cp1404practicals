FILENAME = "subject_data.txt"

def main():
    data = load_data()
    print(data)  # Print the nested list
    display_subject_details(data)  # Call the new function to display details

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    # Create an empty list to store the data as a list of lists
    subject_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        subject_data.append(parts)  # Append the parts as a list to subject_data
    input_file.close()
    return subject_data  # Return the nested list

def display_subject_details(data):
    """Display subject details formatted as requested."""
    for subject_details in data:
        subject_code, lecturer, num_students = subject_details
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")

main()