"""
The for-loop functions for Lab 14.

These functions all require for-loops.

Initial skeleton by W. White (wmw2)

Sungmin Park, sp936
14/07/21
"""


# IMPLEMENT BOTH OF THESE FUNCTIONS

def lesser_than(alist,value):
    """
    Returns the number of elements in alist strictly less than value

    Example: lesser_than([5, 9, 1, 7], 6) evaluates to 2

    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list of ints

    Parameter value:  the value to compare to the list
    Precondition:  value is an int
    """
    count = 0
    for i in alist:
        if i < value:
            count = count+1

    return count


def clamp(alist,min,max):
        """
        Returns: a COPY of the input list, but modified such that every element is
        between min and max.

        Any number in the list less than min is replaced with min.  Any number
        in the list greater than max is replaced with max. Any number between
        min and max is left unchanged.

        Examples:
        >>> clamp([-1, 1, 3, 5],0,4)
        [0,1,3,4]

        Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
        Precondition: alist is a list of numbers (float or int)

        Parameter min: the minimum value for the list
        Precondition: min <= max is a number

        Parameter max: the maximum value for the list
        Precondition: max >= min is a number
        """
    for i in range(len(alist)):
        if max <= alist[i] <= min:
            alist = alist

    return alist
