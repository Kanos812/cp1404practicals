from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Conversion functions
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0 / 9

# Define the route for the home page
@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

# Define the route for the greet page
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

# Define the route for Celsius to Fahrenheit conversion
@app.route('/convert/celsius/<celsius>')
def convert_celsius(celsius):
    try:
        celsius_value = float(celsius)
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        return f"<h1>{celsius_value} Celsius is equal to {fahrenheit_value:.2f} Fahrenheit.</h1>"
    except ValueError:
        return "<h1>Invalid input. Please enter a valid number.</h1>"

# Define the route for Fahrenheit to Celsius conversion
@app.route('/convert/fahrenheit/<fahrenheit>')
def convert_fahrenheit(fahrenheit):
    try:
        fahrenheit_value = float(fahrenheit)
        celsius_value = fahrenheit_to_celsius(fahrenheit_value)
        return f"<h1>{fahrenheit_value} Fahrenheit is equal to {celsius_value:.2f} Celsius.</h1>"
    except ValueError:
        return "<h1>Invalid input. Please enter a valid number.</h1>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
