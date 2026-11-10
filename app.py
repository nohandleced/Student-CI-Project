"""
Name:       Cedric Johnson
Class:      CMSC 426 - Software as a Service
Instructor: Dr. Gyeera
Assignment: In-Class Activity #3 - Building an Automated CI Pipeline
            Using Jenkins and GitHub
Date:       11/09/2026

Description:
    Small calculator application used to demonstrate Continuous
    Integration with Jenkins. Jenkins runs the unit tests in
    tests/test_app.py every time code is pushed to GitHub.
"""


def add_numbers(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract_numbers(a, b):
    """Return a minus b."""
    return a - b


# Runs only when the file is executed directly (not when imported by tests)
if __name__ == "__main__":
    print("Application started")
    print("2 + 3 =", add_numbers(2, 3))
    print("5 - 2 =", subtract_numbers(5, 2))
