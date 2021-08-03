"""
A module with several recursive functions

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


def replace(thelist,a,b):
    """
    Returns a COPY of thelist but with all occurrences of a replaced by b.

    Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """
    if len(thelist)==0: return []
    if thelist[0] == a: r = [b]
    else: r = [thelist[0]]
    return r + replace(thelist[1:], a, b)

def remove_first(thelist, v):
    """
    Returns a COPY of thelist but with the FIRST occurrence of v removed (if present).

    Note: This can be done easily using index. Don't do that.
    Do it recursively.

    Parameter thelist: the list to search
    Precondition: thelist is a list of ints

    Parameter v: the value to search for
    Precondition: v is an int
    """
    if len(thelist) == 0:
        return []
    if thelist[0] == v:
        return thelist[1:]
    else:
        return [thelist[0]] + remove_first(thelist[1:],v)
