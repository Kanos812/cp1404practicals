# Constants
MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = True  # Toggle between True and False for special character requirement
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")

    password = input("> ")

    # Loop until a valid password is entered
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""

    # Check password length
    if not MIN_LENGTH <= len(password) <= MAX_LENGTH:
        return False

    # Initialize counters
    number_of_lower = number_of_upper = number_of_digit = number_of_special = 0

    # Loop through the password and count character types
    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    # Validate character requirements
    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    # If all checks pass, return True
    return True

if __name__ == "__main__":
    main()