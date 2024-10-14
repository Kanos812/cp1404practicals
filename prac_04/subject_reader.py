FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        # Check if the line has enough elements
        if len(parts) >= 3:
            parts[2] = int(parts[2])
            subject_details.append(parts)
        else:
            print(f"Skipping invalid line: {line}")  # Print a message for debugging
    input_file.close()
    return subject_details

def display_subject_details(data):
    """Display subject details in a user-friendly format."""
    for subject_info in data:
        subject_code, lecturer, num_students = subject_info
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")

main()