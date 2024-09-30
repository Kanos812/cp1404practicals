def main():
    min_pass_length = 6
    password = ""

    # Loop until the password meets the length requirement
    while len(password) < min_pass_length:
        password = input(f"Please input a password of at least {min_pass_length} characters: ")
        if len(password) < min_pass_length:
            print(f"Password too short. Please try again.")

    # Print asterisks equal to the length of the password
    print("*" * len(password))
    print("Password accepted. Thank you")


if __name__ == "__main__":
    main()

print("Process concluded.")
