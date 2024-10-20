def extract_name_from_email(email):
    """Extract name from given email"""
    local_part = email.split('@')[0]
    name_parts = local_part.split('.')
    name = " ".join(word.title() for word in name_parts)
    return name


def main():
    """Store emails and names in a dictionary with user confirmation."""
    email_dict = {}  # Initialize an empty dictionary to store emails and names

    while True:
        email_address = input("Please input an email address: ")
        if email_address.lower() == '':
            break  # Exit the loop if the user types 'done'

        name = extract_name_from_email(email_address)
        print(f"Extracted name: {name}")

        # User confirmation
        confirmation = input(f"Is the name '{name}' correct for the email '{email_address}'? (Y/N): ")
        if confirmation.upper() == 'Y' or confirmation == '':
            email_dict[email_address] = name  # Store the email and name in the dictionary
            print("Email and name added to the dictionary.")
        else:
            corrected_name = input('Please input your name: ')
            email_dict[email_address] = corrected_name
            print("Email and name added to the dictionary.")

    return email_dict  # Return the dictionary


if __name__ == "__main__":
    email_dict = main()  # assign returned value to email_dict
    print("\nEmail Dictionary:")
    for email, name in email_dict.items():
        print(f"{email}: {name}")
