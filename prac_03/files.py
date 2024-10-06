# Code 1: Writing user input to a file
file_one_name = "name.txt"
name = input("What is your name? ")  # Get the user's name

# Using 'with' to open the file ensures it gets closed automatically after the block
with open(file_one_name, 'w') as file_one_output:
    print(name, file=file_one_output, end='')  # Write name to the file without adding extra new lines

# Code 2: Reading and greeting with the name from the file
with open(file_one_name, 'r') as file_one_read:
    name_in_file = file_one_read.read().strip()  # Strip any accidental extra spaces/newlines
    print(f"Hi {name_in_file}!")  # Greet the user with their name

# Code 3: Reading numbers from a file and calculating sums
file_two_name = "numbers.txt"
txt_numbers = []

# Using 'with' to handle file reading, ensuring it's properly closed
with open(file_two_name, 'r') as file_two:
    for line in file_two:
        txt_numbers.append(int(line.strip()))  # Convert each line to int and add to the list

# Calculate and print the sum of the first two lines
first_two_lines_sum = txt_numbers[0] + txt_numbers[1]
print(f"Sum of first two lines: {first_two_lines_sum}")

# Calculate and print the sum of all the lines
all_lines_sum = sum(txt_numbers)
print(f"Sum of all lines: {all_lines_sum}")