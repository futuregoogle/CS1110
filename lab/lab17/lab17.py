"""
The for-loop function for Lab 17.

This function requires a loop over a dictionary.

Initial skeleton by W. White (wmw2)

Sungmin Park, sp936
17/07/21
"""


# IMPLEMENT ALL THIS FUNCTION


def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This
    function returns a new dictionary with netids for keys and letter grades
    (strings) for values.  Our cut-off is 90 for an A, 80 for a B, 70 for a C,
    60 for a D.  Anything below 60 is an F.

    Example:  letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) evaluates
    to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.

    Parameter adict: the dictionary of grades
    Precondition: adict is a dictionary with string keys, int values
    """
    # HINT: You will need a dictionary that acts as an accumulator
    # Start with result = {}.  Then add to this dictionary.
    result = {}

    for key in adict:
        if adict[key] >= 90:
            result[key] = 'A'
        elif adict[key] >= 80:
            result[key] = 'B'
        elif adict[key] >= 70:
            result[key] = 'C'
        elif adict[key] >= 60:
            result[key] = 'D'
        else:
            result[key] = 'F'
    return result
