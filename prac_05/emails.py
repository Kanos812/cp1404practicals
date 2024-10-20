def extract_name_from_email(email):
    """Extract name from given email"""

    # Extract snippet before '@'
    local_part = email.split('@')[0]

    # Split local part by periods
    name_parts = local_part.split('.')

    # Convert to proper title case
    name = " ".join(word.title() for word in name_parts)

    # Return extracted name
    return name

email_address = input("Please input an email address: ")
name = extract_name_from_email(email_address)
print(f"The name associated with the email is: {name}")