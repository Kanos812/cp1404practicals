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

menu_choice = ""  # Initialise menu choice

def display_taxis(taxis):
    """Display a numbered list of taxis."""
    for i, Taxi in enumerate(taxis):  #Iterate over taxis list
        print(f"{i} - {Taxi}")

#TODO: Clean up - not functioning properly

while menu_choice != "q":
    print("Please select an Option: "
          "\n (q)uit"
          "\n (c)hoose a taxi "
          "\n (d)rive taxi")
    menu_choice = input(">>>").lower()
    if menu_choice == "c":
        print("Taxis available: ")
        display_taxis(Taxi)
        taxi_choice = int(input("Please choose a taxi: "))
        try:
            current_taxi = taxis[taxi_choice]
        except IndexError:
            print("Invalid taxi choice")
    elif menu_choice == "d":
        if current_taxi:
            distance = float(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            total_bill += trip_cost
        else:
            print("You need to choose a taxi before you can drive")
    elif menu_choice == "q":
        print("Program exiting. Thank you.")
        break
    else:
        print("Invalid option")

#TODO: Convert to dictionary???

# Final Output
# Print total trip cost message
# Print "Taxis are now:"
# Display taxis using display_taxis function

# display_taxis function
# For each taxi in the taxis list:
# Print taxi number and details using __str__ method
