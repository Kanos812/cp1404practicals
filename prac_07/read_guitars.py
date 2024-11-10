"""
CP1404 Practical
File Reader for guitars.csv - opens/reads a file, stores in objects of custom class
Harrison O'Kane
"""

from guitar import Guitar

def main():
    """Read guitar data from file and store in list of Guitar objects."""

    guitars = [] #Create an initially empty list

    try:
        with open('guitars.csv', 'r') as file: #Open file to be read
            for line in file:
                parts = line.strip().split(',') #Split line into parts
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])

                guitar = Guitar(name, year, cost) #Create guitar object
                guitars.append(guitar) #Add created object to list

    except FileNotFoundError:
        print('Error - File not Found') #Error handling in case of missing file

if __name__ == '__main__':
    main()