"""
CP1404 Practical 09
Silver Service Taxi
Harrison O'Kane
21/11/2024
"""

from prac_09.car import Car

class SilverServiceTaxi(Car):
    """Initialise SilverServiceTaxi instance."""
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = 1.23 * fanciness

def get_fare(self):
    """Return fare for trip."""
    return self.flagfall + super().get_fare()