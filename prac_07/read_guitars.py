"""
CP1404 Practical
File Reader for guitars.csv - opens/reads a file, stores in objects of custom class
Harrison O'Kane
"""

from guitar import Guitar

def get_guitars():
    """Allow user to input new guitar data to be saved and stored to the csv file"""
    new_guitars = []
    print("Enter new guitar details (or leave blank to quit):")
    name = input("Name: ")
    while name != "":
        while True:  # Loop until valid year input
            try:
                year = int(input('Year: '))
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid year (number).")

        while True:  # Loop until valid cost input
            try:
                cost = float(input('Cost: '))
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid cost (number).")

        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar} added!")
        name = input("Name: ")  # Get name for next guitar, allowing blank to quit
    return new_guitars

def load_guitars():
    """Read guitar data from file and store in list of Guitar objects."""
    guitars = []
    try:
        with open('guitars.csv', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
                guitars.append(guitar)
    except FileNotFoundError:
        print('Error - File not Found')
    return guitars


def display_guitars(guitars):
    """Display the guitars in the list."""
    print('These are my guitars:')
    for guitar in guitars:
        print(guitar)

def save_guitars(guitars):
    """Save the guitars to the CSV file."""
    with open('guitars.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def main():
    """Main function to orchestrate the program."""
    guitars = load_guitars()
    new_guitars = get_guitars()
    guitars.extend(new_guitars)
    guitars.sort()
    display_guitars(guitars)
if __name__ == '__main__':
    main()