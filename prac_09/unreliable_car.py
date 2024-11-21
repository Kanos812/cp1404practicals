"""
CP1404 Practical 09
Unreliable Car
Harrison O'Kane
21/11/2024
"""

from prac_09.car import Car
import random

class UnreliableCar(Car):
    "Create a class for an Unreliable Car example."

    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar instance."""
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Allow the car to drive if reliability permits it to do so."""

        if random.randint(0,100) < self.reliability: #'Check' reliability
            distance_driven = super().drive(distance) #Drive car if reliability holds up
            return distance_driven
        else:
            return 0 #Car did not drive