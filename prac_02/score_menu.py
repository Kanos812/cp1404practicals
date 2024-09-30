""" Program to Take Score, Categorize Score and Convert to Stars """

def display_menu():
    """ Display the menu options """
    MENU = """
    H - Give score (must be between 0 and 100)
    P - Print score result
    S - Print as many stars as the score
    Q - Quit
    """
    print(MENU)

def get_score():
    """ Get a valid score from the user """
    while True:
        try:
            score = int(input("Please input your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Your score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def star_print(length):
    """ Return a string of stars based on the given length """
    return "*" * length

def score_categorizer(score):
    """ Categorize the score """
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Good"
    else:
        return "Bad"

def main():
    """ Main program to manage user interactions and scoring """
    inp_score = None
    display_menu()

    while True:
        choice = input(">>> ").upper()

        if choice == "Q":
            break

        elif choice == "H":
            inp_score = get_score()

        elif choice == "P":
            if inp_score is not None:
                print("Your score is:", score_categorizer(inp_score))
            else:
                print("You must give a score first (H).")

        elif choice == "S":
            if inp_score is not None:
                print(star_print(inp_score))
            else:
                print("You must give a score first (H).")

        else:
            print("Invalid selection. Please choose again.")

        display_menu()

    print("Process concluded.")

if __name__ == "__main__":
    main()
