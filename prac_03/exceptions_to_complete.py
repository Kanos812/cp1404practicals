# Loop continues until a valid integer is entered
is_finished = False
while not is_finished:
    try:
        # Prompt user for a valid integer
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit loop if input is a valid integer
    except ValueError:
        # Error message for non-integer inputs
        print("Please enter a valid integer.")

# Output the result after successful input
print("Valid result is:", result)