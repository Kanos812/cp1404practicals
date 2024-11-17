"""
CP1404 Practical
Miles to KM Conversion
Harrison O'Kane
17/11/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

conversion_factor = 1.609344 #Mile to Kilometres

class ConverterApp(App):
    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')  # Load the KV file
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            kilometers = miles * conversion_factor
            self.root.ids.output_label.text = f"{kilometers:.2f} kilometers"
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

if __name__ == '__main__':
    ConverterApp().run()
