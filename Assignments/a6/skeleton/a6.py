"""Module with functions to implement for Assignment 6.

This module holds four functions. You need to implement each of these. Your
tests should be written in a6est.py.

As always, you should look at the docstrings CAREFULLY when implementing these
functions. Be sure not to forget any of the points mentioned there.

AUTHOR: sp936
"""


# PART A
def binary_search(numbers, n):
    """Returns True if n appears in numbers, False otherwise.

    This function performs a binary search on the list numbers. The details of
    binary search are explained in the assignment PDF.

    This function MUST be implemented recursively.

    Precondition: numbers is a sorted list of integers, n is an integer.

    Examples:
    >>> binary_search([0, 2, 5, 8, 10, 42, 101], 101)
    True
    >>> binary_search([2, 3, 5, 7, 11, 13, 17, 19], 9)
    False
    >>> binary_search([1, 1, 2, 3, 5, 8, 13, 21, 34], 1)
    True
    >>> binary_search([0, 0, 5, 28, 9001], 91)
    False
    """
    # IMPLEMENT ME
    l = len(numbers)
    if l == 0:
        return False
    curr = numbers[l//2]
    if curr == n:
        return True

    if curr < n:
        return binary_search(numbers[l//2 + 1 : ], n)
    if curr > n:
        return binary_search(numbers[ : l//2], n)

# PART B
def revert(thelist):
    """Returns the reverse of thelist.

    The reverse is the same list, except read from the end to the beginning.
    This function MUST NOT change the input.

    This function MUST be implemented recursively.

    Precondition: thelist is a list.

    Examples:
    >>> revert([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> revert(['A', 'man', 'a', 'plan', 'a', 'canal', 'Panama'])
    ['Panama', 'canal', 'a', 'plan', 'a', 'man', 'A']
    >>> revert(['Sator', 'Arepo', 'Tenet', 'Opera', 'Rotas'])
    ['Rotas', 'Opera', 'Tenet', 'Arepo', 'Sator']
    """
    # IMPLEMENT ME
    if len(thelist) == 0:
        return []
    return [thelist[-1]] + revert(thelist[:-1])

def gray_code(bits):
    """Returns the list of Gray codes for n bits.

    A single Gray code is encoded as a list of booleans, read from left to
    right. A zero is represented by False, while a one is represented by True.
    The details of how to compute the Gray code for n bits from the Gray code
    for n-1 bits are explained in the assignment PDF.

    This function MUST be implemented recursively.

    Precondition: bits is an integer, which is at least zero.

    Examples:
    >>> gray_code(0)
    [[]]
    >>> gray_code(2)
    [[False, False], [False, True], [True, True], [True, False]]
    >>> gray_code(3)  # output split over multiple lines for readability
    [[False, False, False],
     [False, False, True],
     [False, True, True],
     [False, True, False],
     [True, True, False],
     [True, True, True],
     [True, False, True],
     [True, False, False]]
    """
    # IMPLEMENT ME
    if bits == 0:
        return [[]]
    old_list = gray_code(bits-1)
    old_reverted = revert(old_list)

    output = []
    for elem in old_list:
        output.append([False]+[x for x in elem])
    for elem in old_reverted:
        output.append([True]+[x for x in elem])

    return output


# PART C
def approx_sqrt(number, tolerance):
    """Returns an approximation of the square root of number, such that the
    difference between the square root of the approximation and number is at
    most the tolerance.

    To compute the approximation, this function uses Newton's method. The
    details of Newton's method are explained in the assignment PDF.

    This function may get stuck for very small values of tolerance, due to the
    numerical imprecision that comes with floats.

    Precondition: number and tolerance are nonnegative floats.

    Examples (your outcomes may vary depending on your initial guess)
    >>> approx_sqrt(2, 0.0001)
    1.4142156862745099
    >>> approx_sqrt(123, 0.001)
    11.090536508032852
    >>> approx_sqrt(91823, 0.005)
    303.0231014306778
    """
    # IMPLEMENT ME
    xi = 0
    while xi**2 < number:
        xi += 1

    while abs(xi**2 - number) > tolerance:
        xi = xi - ((xi**2 - number) / (2 * xi))

    return xi
