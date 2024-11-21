"""
CP1404 Practical 09
Band Class
Harrison O'Kane
21/11/2024
"""
from prac_09 import musician


class Band:
    """Band class to manage collection of musicians."""

    def __init__(self, name=""):
        """Initialize band collection."""
        self.name = name
        self.musicians = []

    def _str_(self):
        """Return string representation of band collection."""
        return f"{self.name}"

    def add(self, musician):
        """Add a musician."""
        self.musicians.append(musician)

    def play(self):
        "Return a string of each musician and their instrument."
        return"Test"