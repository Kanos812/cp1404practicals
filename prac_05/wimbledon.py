def main():
    """Read data from CSV file and display processed information."""
    filename = "wimbledon.csv"
    champions_data = load_data(filename)

    display_champions(champions_data)

def load_data(filename):
    """Read CSV file and return a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data

def display_champions(data):
    """Display champions and their win counts."""
    champions_wins = {}
    for row in data[1:]:
        champion = row[2]
        champions_wins[champion] = champions_wins.get(champion, 0) + 1

    print("Wimbledon Champions: ")
    for champion, wins in champions_wins.items():
        print(f"{champion} {wins}")

if __name__ == "__main__":
    main()