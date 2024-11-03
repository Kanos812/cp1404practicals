"""
Guitars! - CP1404 Practical
Harrison O'Kane
Started - 1831
Estimated Time - 35 Mins
Estimated Completion - 1906
Actual Completion -

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
        current_year = 2023
        return current_year - self.year