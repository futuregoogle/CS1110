"""Module to simulate cellular automata.

The functions in this file have a docstring, but no implementation. Read each
docstring *CAREFULLY* and implement the function.

For details and additional information on how to implement each function,
refer to the assignment description.

AUTHOR: YOUR NETID HERE
"""

import random


# PART A
def byte_to_number(byte):
    """Converts byte to the corresponding integer.

    The most significant bit is first in the input list. This function should
    be the inverse of number_to_byte on lists of size 8.

    Precondition: byte is a list of *exactly* 8 boolean values.

    Raises TypeError if byte is not a list.

    Examples:
    >>> byte_to_number([False, True, True, True, True, False, True, True])
    123
    >>> byte_to_number([False, True, True, False, True, True, True, False])
    110
    >>> byte_to_number([True, False, False, False, False, False, False, False])
    128
    """
    # IMPLEMENT ME


def number_to_byte(number):
    """Converts number to a list of exactly 8 booleans representing its bits.

    The most significant bit comes first in the resulting list.

    Precondition: number is an integer greater than or equal to zero, and less
    than or equal to 255, so that the number fits in a byte.

    Raises TypeError if number is not an int.
    Raises ValueError if number is out of range.

    Examples:
    >>> number_to_byte(123)
    [False, True, True, True, True, False, True, True]
    >>> number_to_byte(110)
    [False, True, True, False, True, True, True, False]
    >>> number_to_byte(128)
    [True, False, False, False, False, False, False, False]
    """
    # IMPLEMENT ME


# PART B
def next_cell(pattern, rule):
    """Returns the new cell bit given its neighbours and the rule to apply.

    Precondition: pattern is a list of *exactly* three booleans representing
    the neighbours of the current cell; rule is a non-negative number less than
    or equal to 255.

    Examples:
    >>> next_cell([True, False, True], 110)
    True
    >>> next_cell([False, False, True], 21)
    False
    >>> next_cell([False, True, True], 184)
    True
    """
    bits = number_to_byte(rule)
    pnum = byte_to_number([False] * 7 + pattern)
    return bits[7 - pnum]


def next_generation(line, rule):
    """Computes the new generation of cells, given current cells and the rule.

    Precondition: line is a list of booleans, rule is an integer.

    Raises TypeError if line is not a list.
    Raises TypeError if rule is not an integer.

    Examples:
    >>> next_generation([True, True, True, False], 110)
    [True, False, True, True]
    >>> next_generation([False, False, True, True], 21)
    [True, False, False, False]
    >>> next_generation([True, False, False, True], 42)
    [False, False, True, True]
    """
    # IMPLEMENT ME


# PART C
def random_generation(length):
    """Returns a random list of booleans of size length.

    Precondition: length is an integer.

    Examples:
    >>> random_generation(5)
    [True, True]
    >>> random_generation(2)
    [True, False, False, True, False]
    """
    line = []
    for i in range(length):
        cell = random.randint(0, 1) == 1
        line.append(cell)
    return line


def print_generation(line):
    """Prints the generation in line, with '[]' representing a cell that lives,
    and '  ' (two spaces) representing a cell that is dead.

    Precondition: line is a list of booleans.

    Raises TypeError if line is not a list.

    Examples:
    >>> print_generation([True, True, False, True])
    [][] []
    >>> print_generation([False, False, True, False, True])
      [] []
    >>> print_generation([False, True, True, False])
     [][]
    """
    # IMPLEMENT ME
