"""
CP1404 Practical 09
Band Class
Harrison O'Kane
21/11/2024
"""

import musician

class Band:
    """Band class to manage collection of musicians."""

    def __init__(self, name=""):
        """Initialize band collection."""
        self.name = name
        self.musicians = []

    def _str_(self):
        """Return string representation of band collection."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician."""
        self.musicians.append(musician)

    def play(self):
        "Return a string of each musician and their instrument (if available)."
        return '\n'.join(musician.play() for musician in self.musicians)