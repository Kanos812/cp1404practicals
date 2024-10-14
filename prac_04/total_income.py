def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)  # Call the print_report function

def print_report(incomes):
    """Print the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    num_months = len(incomes)  # Determine num_months from incomes list
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

if __name__ == "__main__":
    main()  # Call the main function to start the program