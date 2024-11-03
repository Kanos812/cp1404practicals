from guitar import Guitar

def main():
    """ Get guitar details"""
    guitars = []

    # Get guitar details from user
    name = input("Input Guitar Name (or leave blank to view list): ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, "added")
        name = input("Name: ")

    # Display guitar details
    print("\n... snip ...\n")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage) " if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()
