"""
Programming Languages - CP1404 Practical
Harrison O'Kane
Started - 1742 03/11/24
Estimated Time - 25 Mins
Estimated Completion - 1607
Actual Completion -

"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name="", typing="", reflection="", year=""):
        """Initialize a ProgrammingLanguage object instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

def is_dynamic(self):
    """Determine if language is dynamically typed."""
    return self.typing == "Dynamic"

def __str__(self):
    """Return string representation of language."""
    return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"
