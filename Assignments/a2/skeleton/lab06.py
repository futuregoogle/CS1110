"""
'The module for first_inside_quotes'

Name:Sungmin Park, net-id:sp936
Date: 28/06/2021
"""
import sys

def first_inside_quotes(s):
    """
    Returns: The first substring of s between two (double) quote characters.

    A quote character is one that is inside a string, not one that delimits it.
    We typically use single quotes (') to delimit a string if want to use a double
    quote character (") inside of it.

    Example:  If s is 'A "B C" D', this function returns 'B C'
    Example:  If s is 'A "B C" D "E F" G', this function still returns 'B C'
    because it only picks the first such substring.

    Parameter s: a string to search
    Precondition: s a string with at least two (double) quote characters.
    """
    start = s.find('"')
    end = s.find('"', start+1)

    return s[start+1:end]
