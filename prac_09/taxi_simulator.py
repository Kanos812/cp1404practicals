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
    for i, taxi in enumerate(taxis):  #Iterate over taxis list
        print(f"{i} - {taxi}")

"""Menu Directory."""
menu = {
    "q": {"description": "Quit", "function": None},  # Quit has no function
    "c": {"description": "Choose taxi", "function": choose_taxi},
    "d": {"description": "Drive", "function": drive_taxi},
}

while True:
    print("Please select an Option: "
          "\n (Q)uit"
          "\n (C)hoose a taxi "
          "\n (D)rive taxi")
    menu_choice = input(">>> ").lower()
    if menu_choice in menu:
        if menu_choice == "q":
            print("Program Exiting. Thank You...")
            break  # Exit loop if choice is 'q'
        else:
            action = menu[menu_choice]["function"]
            if action:
                if action == choose_taxi:
                    current_taxi = action(taxis)  # Pass taxis to choose_taxi
                else:
                    trip_cost = action(current_taxi)  # Pass current_taxi to drive_taxi
                    total_bill += trip_cost
    else:
        print("Invalid option")