"""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

# Use for loop to interate through 'CODE_TO_NAME' dictionary and print formatted

for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code} is {state_name}")

# User input for conversion

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code.upper()])
    except:
        print("Invalid short state")
    state_code = input("Enter short state: ")


