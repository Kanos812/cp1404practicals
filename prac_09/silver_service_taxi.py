"""
CP1404 Practical 09
Silver Service Taxi
Harrison O'Kane
21/11/2024
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Initialise SilverServiceTaxi instance."""
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = 1.23 * fanciness

def get_fare(self):
    """Return fare for trip."""
    return super().get_fare()