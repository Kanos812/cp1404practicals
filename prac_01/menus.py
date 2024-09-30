def display_menu():
    """Display the menu options."""
    MENU = """  H - Hello
                G - Goodbye
                Q - Quit """

    print(MENU)

def main():
    """Main function to greet the user based on their menu choice."""
    # Get the user's name
    name_input = input("What is your name? ").capitalize()

    # Print the menu
    display_menu()

    # Get the user's choice and convert to uppercase
    choice = input("Please select an option from the menu: ").upper()

    # Loop while the choice is not "Q" (quit)
    while choice != "Q":
        # Greet if the user chooses "H"
        if choice == "H":
            print(f"Hello, {name_input}!")
        # Say goodbye if the user chooses "G"
        elif choice == "G":
            print(f"Goodbye, {name_input}!")
        # Handle invalid inputs
        else:
            print("Invalid input. Please choose a valid option.")

        # Display the menu again
        display_menu()

        # Ask for the next choice
        choice = input("Please select an option from the menu: ").upper()

    # When "Q" is chosen, end the program
    print("Process concluded. Goodbye!")

# Run the program
if __name__ == "__main__":
    main()
