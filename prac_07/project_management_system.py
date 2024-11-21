"""
Project Management System
Expected Time to Complete - 01:15
Actual Time To Complete - 0:30
Submitted Late - 22/11/24
Harrison O'Kane
"""

import datetime
import csv


class Project:
    """Represents a project with name, start date, priority, and completion."""

    def __init__(self, name, start_date, priority, completion=False, completion_percentage=None):
        """Initialize a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.completion = completion
        self.completion_message = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, completion: {self.completion}"

    def __lt__(self, other):
        """Less than comparison for sorting."""
        return self.priority < other.priority

    def add_project(self, project):
          """Add a new project."""
        name = input("Name: ")
        while True:
            try:
                start_date_str = input("Start date (dd/mm/yyyy): ")
                start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Invalid date format. Please use dd/mm/yyyy.")
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: "))
        completion_percentage = int(input("Percent complete: "))

        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)
        print(f"{project.name} added.")


    def delete_project(projects):
        """Delete a project by its name."""
        # Display numbered list of projects for user to choose from
        for i, project in enumerate(projects):
            print(f"{i} {project}")

        while True:  # Loop until valid project index is entered
                try:
                    project_index = int(input("Enter the number of the project to delete: "))
                    if 0 <= project_index < len(projects):
                        break
                    else:
                        print("Invalid project number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")


    def update_project(projects):
        """Update an existing project."""
        # Display numbered list of projects for user to choose from
        for i, project in enumerate(projects):
            print(f"{i} {project}")

        while True:  # Loop until valid project index is entered
            try:
                project_index = int(input("Enter the number of the project to update: "))
                if 0 <= project_index < len(projects):
                    break
                else:
                    print("Invalid project number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        project = projects[project_index]
        print(project)  # Display the selected project

# Get new completion percentage from the user
    while True:
        try:
            new_completion_percentage = input("New Percentage: ")
            if new_completion_percentage == "":
                break  # Leave blank to keep existing value
            new_completion_percentage = int(new_completion_percentage)
            if 0 <= new_completion_percentage <= 100:
                project.completion_percentage = new_completion_percentage
                break
            else:
                print("Invalid percentage. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get new priority from the user
    while True:
        try:
            new_priority = input("New Priority: ")
            if new_priority == "":
                break  # Leave blank to keep existing value
            new_priority = int(new_priority)
            project.priority = new_priority
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Project updated successfully.")

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


def load_projects(filename="projects.txt"):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        for row in reader:
            name, start_date_str, priority, cost_estimate, completion_percentage = row
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            completion_percentage = int(completion_percentage)
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects

def save_projects(projects, filename="projects.txt"):
    """Save projects to a file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])  # Header
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime("%d/%m/%Y"), project.priority, project.cost_estimate, project.completion_percentage])

def filter_projects_by_date(projects, date):
    """Filter projects by start date."""
    return [project for project in projects if project.start_date > date]
