COLOUR_CODES = {
    "crimson": "#DC143C",
    "teal": "#008080",
    "coral": "#FF7F50",
    "slategray": "#708090",
    "turquoise": "#40E0D0",
    "goldenrod": "#DAA520",
    "lavender": "#E6E6FA",
    "royalblue": "#4169E1",
    "tomato": "#FF6347",
    "sienna": "#A0522D"
}

colour_name = input("Enter a color name (or leave blank to stop): ").lower()

while colour_name != "":
    try:
        hex_code = COLOUR_CODES[colour_name]
        print(f"The hex code for {colour_name} is {hex_code}")
    except KeyError:
        print("Invalid color name.")
    colour_name = input("Enter a color name (or leave blank to stop): ").lower()
