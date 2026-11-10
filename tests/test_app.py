"""
Name:       Cedric Johnson
Class:      CMSC 426 - Software as a Service
Instructor: Dr. Gyeera
Assignment: In-Class Activity #3 - Jenkins CI Pipeline
Date:       11/09/2026

Description:
    Unit tests for app.py. Jenkins runs these automatically on every build.
    If any test fails, the build is marked as FAILED.
"""
import unittest

from app import add_numbers, subtract_numbers


class TestCalculator(unittest.TestCase):
    # Checks the main example from the assignment: 2 + 3 = 5
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    # Checks that adding a negative number works
    def test_add_negative(self):
        self.assertEqual(add_numbers(-1, 1), 0)

    # Checks basic subtraction: 5 - 2 = 3
    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 2), 3)


if __name__ == "__main__":
    unittest.main()
