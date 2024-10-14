def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes)

def print_report(incomes):
    """Print the income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0  # Initialize total to 0
    for month, income in enumerate(incomes, 1):  # Iterate using enumerate
        total += income  # Update total cumulatively
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

if __name__ == "__main__":
    main()
