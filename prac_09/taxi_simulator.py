"""
CP1404 Practical 09
Taxi Simulator
Harrison O'Kane
22/11/2024
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

"""Initialisation."""
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
current_taxi = None
total_bill = 0

# Main Loop
# Print welcome message and menu options
# Get user input for menu_choice
# While menu_choice is not "q":
    # If menu_choice is "c":
        # Display available taxis using display_taxis function
        # Get user input for taxi_choice
        # If taxi_choice is valid:
            # Set current_taxi to the chosen taxi
        # Otherwise, print "Invalid taxi choice"
    # Else if menu_choice is "d":
        # If current_taxi is not None:
            # Get user input for distance
            # Start a new fare for current_taxi
            # Drive current_taxi for the given distance
            # Calculate trip_cost using get_fare method
            # Print trip cost message
            # Add trip_cost to total_bill
        # Otherwise, print "You need to choose a taxi before you can drive"
    # Otherwise:
        # Print "Invalid option"
    # Print current total_bill
    # Print menu options again
    # Get user input for menu_choice

# Final Output
# Print total trip cost message
# Print "Taxis are now:"
# Display taxis using display_taxis function

# display_taxis function
# For each taxi in the taxis list:
    # Print taxi number and details using __str__ method