"""
Even More Guitars! - Week 07 Practical
Harrison O'Kane
"""

class Guitar:
    """Store details of guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of the guitar in years."""
        # Calculate age based on current year (replace with actual current year)
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50+ years old)."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Sort guitars by year"""
        return self.year < other.year