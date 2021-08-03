"""
A module with several recursive functions

Sungmin Park, sp936
07/28/21
"""


# IMPLEMENT ALL OF THESE FUNCTIONS

def sum_list(thelist):
    """
    Returns the sum of the integers in list l.

        Example: sum_list([34]) is 34
        Example: sum_list([7,34,1,2,2]) is 46

    Parameter thelist: the list to sum
    Precondition: thelist is a list of ints
    """
    return thelist[0] + sum_list(thelist[1:]) if thelist else 0


def numberof(thelist, v):
    """
    Returns the number of times v occurs in thelist.

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter v: The value to count
    Precondition: v is an int
    """
    if not thelist:
        return 0
    if thelist[0] == v:
        return 1 + numberof(thelist[1:], v)
    else:
        return numberof(thelist[1:], v)
