"""
A module devoted to exceptions and dynamic typing

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# PART 1
def get_previous(filename):
    """
    Returns the number before the one stored in the file filename.

    By number before, we mean that the number is an int, and the result subtracts one
    from the int in the file.

    If the file does not contain an int, this function returns the contents of the file.

    If the file does not exist or cannot be opened, this function returns None.

    Parameter filename: The name of the file to open
    Precondition: filename is a string
    """
    assert isinstance(filename,str)
    try:
        file = open(filename)
        contents = file.read()
        number=int(contents)
        return number-1
    except FileNotFoundError:
        return None
    except ValueError:
        return contents


# PART 2

def divide_even(number):
    """
    Returns half of the input as an integer, if the number is even.

    Parameter number: the number to divide
    Precondition: number is an even integer

    Raises a ValueError with the message 'number should be even' if the number
    is odd, and a TypeError with the message 'number should be an int' if the
    number is not an integer.
    """
    if not isinstance(number,int):
        raise TypeError("number should be an int")
    if  number % 2 != 0:
        raise ValueError("number should be even")

    if number(int and number%2==0):
        number = number / 2
        return number
