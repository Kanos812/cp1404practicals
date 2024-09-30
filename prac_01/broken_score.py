"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

#get user score as a float input
score = float(input("Enter score: "))
#check boundaries for input

if score >= 0 and score < 50:
    print("Bad")
elif score >= 50 and score < 90:
    print("Passable")
elif score >= 90  and score <= 100:
    print("Excellent")

else:
    print("invalid score")