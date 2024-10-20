def main():
    """Read data from CSV file and display processed information."""
    filename = "wimbledon.csv"
    champions_data = load_data(filename)

 # Print the list of lists
    for row in champions_data:
        print(row)

def load_data(filename):
    """Read CSV file and return a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data

if __name__ == "__main__":
    main()