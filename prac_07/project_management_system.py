"""
Project Management System
Started 23:30 (I should have not left this so late...)
Expected Time to Completion - 30 Mins
Finished 
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

    def add_project(self, project):
        """Add a new project to the system."""
        self.projects.append(project)

    def delete_project(self, project_name):
        """Delete a project from the system."""
        for i, project in enumerate(self.projects):
            if project.name == project_name:
                del self.projects[i]
                return True
        return False  # Project not found