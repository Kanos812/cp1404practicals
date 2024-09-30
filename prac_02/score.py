def score_categorizer(score):
    """ Categorize the score """
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Good"
    else:
        return "Bad"

def main():
    """ Main program to categorize the score """
    try:
        score = int(input("Please input your score: "))
        if 0 <= score <= 100:
            category = score_categorizer(score)
            print(f"Your score is: {category}")
        else:
            print("Your score must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
