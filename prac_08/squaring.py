"""
CP1404 Practical
Kivy GUI program to square a number
Harrison O'Kane, IT@JCU
Started 17/11/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Harrison O'Kane"


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            number = float(value) #Attempt conversion to float
            result = number ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid Input"


SquareNumberApp().run()
