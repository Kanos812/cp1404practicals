from guitar import Guitar

def main():
    """ Get guitar details"""
    guitars = []

    # Get guitar details from user
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, "added")
        name = input("Name: ")

if __name__ == "__main__":
    main()
