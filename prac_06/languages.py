"""
Programming Languages - CP1404 Practical
Harrison O'Kane
Started - 1742 03/11/24
Estimated Time - 25 Mins
Estimated Completion - 1807
Actual Completion - 1805

"""

from programming_languages import ProgrammingLanguage

""" Language class values """
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

# Create list of languages
languages = [python, ruby, visual_basic]

# Loop to iterate through language list
print("The following are dynamically typed languages:")
for language in languages:
    if language.is_dynamic():
        print(language.name)