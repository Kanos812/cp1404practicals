""" Volatile Stock Price Simulator """

import random

# Constants
FILE_NAME = "capitalist_conrad_output.txt"
MAX_INCREASE = 0.175  # Max 17.5% increase
MAX_DECREASE = 0.05   # Max 5% decrease
MIN_PRICE = 1.00      # Minimum price before simulation stops
MAX_PRICE = 100.00    # Maximum price before simulation stops
INITIAL_PRICE = 10.00 # Starting price

# Initialize variables
price = INITIAL_PRICE
day_count = 1  # Start day from 1

# Open the file to write output
with open(FILE_NAME, 'w') as out_file:
    # Run the simulation until price hits limits
    while MIN_PRICE <= price <= MAX_PRICE:
        # Format and print the daily price
        daily_output = f"On day {day_count} the price is ${price:,.2f}"
        print(daily_output)
        print(daily_output, file=out_file)  # Write to the file as well

        # Determine price change
        if random.randint(1, 2) == 1:
            # Price increases by a random value between 0 and MAX_INCREASE
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # Price decreases by a random value between 0 and MAX_DECREASE
            price_change = random.uniform(-MAX_DECREASE, 0)

        # Update the price
        price *= (1 + price_change)

        # Increment day count
        day_count += 1
