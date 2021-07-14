"""
Function for testing

This module provides a function to show off errors.  You must test it to find the errors.
This module is intended to prepare you for the second assignment.

Authors: sp936
Date:    30/06/2021
"""


def has_a_vowel(s):
    """
    Returns: True if s has at least one vowel (a, e, i, o, or u)

    This function does not count y as a vowel.

    Parameter s: a string to check
    Precondition: s is a non-empty string with all lower case letters

    This function may include intentional errors.
    """
    return 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s
