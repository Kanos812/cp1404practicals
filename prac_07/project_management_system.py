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

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage=0):
        """Initialize a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, cost estimate: {self.cost_estimate}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Less than comparison for sorting."""
        return self.priority < other.priority

# --- Function to add a new project ---
def add_project(projects):
    """Add a new project to the list."""
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
                del projects[project_index]  # Delete the project
                print("Project deleted successfully.")
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


def display_projects(projects):
    """Display projects, grouped by completion status and sorted by priority."""
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    incomplete_projects.sort()  # Sort by priority (due to __lt__ in Project class)
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def load_projects(filename="projects.txt"):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter='\t')  # Use tab delimiter
            next(reader)  # Skip the header line
            for row in reader:
                name, start_date_str, priority, cost_estimate, completion_percentage = row
                start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
                priority = int(priority)
                cost_estimate = float(cost_estimate)
                completion_percentage = int(completion_percentage)
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return projects


def save_projects(projects, filename="projects.txt"):
    """Save projects to a file."""
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter='\t')  # Use tab delimiter
            writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])  # Header
            for project in projects:
                writer.writerow([project.name, project.start_date.strftime("%d/%m/%Y"),
                                 project.priority, project.cost_estimate, project.completion_percentage])
    except IOError as e:
        print(f"Error saving projects to '{filename}': {e}")


def filter_projects_by_date(projects):
    """Filter projects by start date."""
    while True:
        try:
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")

    filtered_projects = [project for project in projects if project.start_date > filter_date]
    filtered_projects.sort(key=lambda project: project.start_date)  # Sort by start date

    for project in filtered_projects:
        print(project)