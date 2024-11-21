"""
Guitars! - CP1404 Practical
Harrison O'Kane

Time Worked - 1831 - 1908 ; 2111 - 2115
Estimated Completion - 0:35
Actual Completion - 0:41 (+0:06)

"""

import datetime

current_year = datetime.date.today().year

class Guitar:
    """Store details of guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar in years."""
        # Calculate age based on current year
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50+ years old)."""
        return self.get_age() >= 50