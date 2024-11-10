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

    def update_project(self, project_name, new_start_date=None, new_priority=None, new_completion=None):
        """Update an existing project."""
        for project in self.projects:
            if project.name == project_name:
                if new_start_date:
                    project.start_date = new_start_date
                if new_priority:
                    project.priority = new_priority
                if new_completion is not None:
                    project.completion = new_completion
                return True
        return False  # Project not found

    def display_projects(self, sort_by="priority"):
        """Display projects, sorted by priority or completion."""
        if sort_by == "priority":
            projects_to_display = sorted(self.projects, key=lambda p: p.priority)
        elif sort_by == "completion":
            projects_to_display = sorted(self.projects, key=lambda p: p.completion)
        else:
            projects_to_display = self.projects

        for project in projects_to_display:
            print(project)