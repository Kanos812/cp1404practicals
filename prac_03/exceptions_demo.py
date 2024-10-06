def get_valid_number(prompt):
    """Get a valid integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; please enter a valid integer.")

def main():
    # Get the numerator and denominator with validation
    numerator = get_valid_number("Enter the numerator: ")
    denominator = get_valid_number("Enter the denominator (cannot be 0): ")

    # Ensure the denominator is not zero
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = get_valid_number("Enter a new denominator: ")

    # Calculate and print the fraction
    fraction = numerator / denominator
    print(f"Result: {fraction}")

# Run the program
if __name__ == "__main__":
    main()

print("Finished.")

# Q1: When will a ValueError occur?
# A1: A ValueError occurs when the user inputs something that cannot be converted to an integer,
#     such as a string or a non-integer value.

# Q2: When will a ZeroDivisionError occur?
# A2: A ZeroDivisionError would occur if the denominator is zero during the division.
#     In the current version of the code, this will not happen because the denominator is checked.

# Q3: Could you change the code to avoid the possibility of a ZeroDivisionError?
# A3: Yes, and the code has been updated to prevent the ZeroDivisionError by continuously prompting
#     the user to input a valid (non-zero) denominator.
