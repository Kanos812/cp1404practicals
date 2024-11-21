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

def choose_taxi(taxis):
    """Choose taxi from list."""
    print("Taxi's available: ")
    display_taxis(taxis)
    taxi_choice = int(input("Please choose a taxi: "))
    try:
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
        return None

def drive_taxi(current_taxi):
    """Drive the current taxi and update the total bill."""
    if current_taxi:
        distance = float(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        return trip_cost
    else:
        print("You need to choose a taxi before you can drive")
        return None

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