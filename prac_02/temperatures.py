""" Temperature Conversion Calculator """

def celsius_to_fahrenheit(temperature):
    """Convert Celsius to Fahrenheit."""
    return (temperature * 1.8) + 32


def fahrenheit_to_celsius(temperature):
    """Convert Fahrenheit to Celsius."""
    return (temperature - 32) / 1.8


def main():
    """Main program to convert temperature based on user's choice."""
    print("Temperature Converter")
    print("1 - Convert Celsius to Fahrenheit")
    print("2 - Convert Fahrenheit to Celsius")

    choice = input("Please input your choice: ")

    # Validate the user's choice
    while choice not in ("1", "2"):
        print("Invalid choice. Please choose 1 or 2.")
        choice = input("Please input your choice: ")

    # Get temperature input from the user and validate it
    try:
        temperature = float(input("Enter the temperature: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the temperature.")
        return  # Exit the program if input is invalid

    # Perform the chosen conversion
    if choice == "1":
        result = celsius_to_fahrenheit(temperature)
        print(f"Result: {result:.2f} F")
    else:
        result = fahrenheit_to_celsius(temperature)
        print(f"Result: {result:.2f} C")


# Run the program
if __name__ == "__main__":
    main()
