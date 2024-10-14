def main():
    # Username authorization
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
                 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

    """Get 5 numbers from the user and display information about them."""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)

    # Output information about the numbers with the specified format
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))



if __name__ == "__main__":
    main()