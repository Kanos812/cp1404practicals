def extract_name_from_email(email):
    """Extract name from given email"""
    local_part = email.split('@')[0]
    name_parts = local_part.split('.')
    name = " ".join(word.title() for word in name_parts)
    return name


def main():
    """Store emails and names in a dictionary with user confirmation."""
    email_dict = {}  # Initialize an empty dictionary to store emails and names

    email_address = input("Please input an email address: ")
    while email_address.lower() != '':

        name = extract_name_from_email(email_address)
        print(f"Extracted name: {name}")

        # User confirmation
        while True:
            confirmation = input(f"Is the name '{name}' correct for the email '{email_address}'? (Y/N): ").upper()
            if confirmation in ("Y", "N", ""):
                break  # Exit inner loop if input is valid
            print("Invalid input. Please enter Y, N, or press Enter.")

        if confirmation == "N":
            corrected_name = input('Please input your name: ')
            email_dict[email_address] = corrected_name
        else:  # Confirmation is 'Y' or '' (default to yes)
            email_dict[email_address] = name
        print("Email and name added to the dictionary.")

        email_address = input("Please input an email address: ")

    return email_dict  # Return the dictionary

if __name__ == "__main__":
    email_dict = main()  # Assign returned value to email_dict
    print("\nEmail Dictionary:")
    for email, name in email_dict.items():
        print(f"{email}: {name}")
