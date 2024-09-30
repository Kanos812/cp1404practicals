"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

#creates indefinite loop
while True:

#Get Input
    user_input = input("Enter sales in AUD or type 'end' to exit): ")

    # Check if the user wants to exit.
    if user_input == 'end':
        print("Thank you for using the program.")
        break

    try:
        # Convert the input to a float for sales calculation.
        sales = float(user_input)

        # Calculate the bonus based on the sales amount.
        if sales >= 1000:
            bonus = sales * 0.15
        elif sales <= 0:
            bonus = 0
        else:
            bonus = sales * 0.10

        print(f"The bonus is: ${bonus:.2f}")

    except ValueError:
        print("Invalid input. Please try again or type 'end' to exit")
    