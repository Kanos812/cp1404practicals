"""
Project Management System
Started 11:30
Expected Time to Completion - 30 Mins
Harrison O'Kane
"""

class Project:
    """Represents a project with name, start date, priority, and completion."""

    def __init__(self, name, start_date, priority, completion=False):
        """Initialize a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.completion = completion

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, completion: {self.completion}"