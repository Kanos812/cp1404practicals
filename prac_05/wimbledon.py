def main():
    """ Read data from CSV file and display processed information """
    filename = "wimbledon.csv"
    champions_data = load_data(filename)

    display_champions(champions_data)
    display_countries(champions_data)


def load_data(filename):
    """ Read CSV file and return a list of lists """
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


def display_champions(data):
    """ Display champions and their win counts """
    champions_wins = {}
    for row in data[1:]:
        champion = row[2]
        champions_wins[champion] = champions_wins.get(champion, 0) + 1

    print("Wimbledon Champions:")
    for champion, wins in champions_wins.items():
        print(f"{champion} {wins}")


def display_countries(data):
    """ Display countries of champions in alphabetical order """
    countries = set()
    for row in data[1:]:
        country = row[1]
        countries.add(country)

    countries_list = sorted(list(countries))
    print("\nThese", len(countries_list), "countries have won Wimbledon:")
    print(", ".join(countries_list))


if __name__ == "__main__":
    main()
