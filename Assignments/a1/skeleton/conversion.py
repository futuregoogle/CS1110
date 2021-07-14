"""
A module for conversions between several units.

Author: sp936
Date:   26/6/2021
"""

def to_centigrade(x):
    """Returns: x degrees Fahrenheit converted to centigrade

    Precondition: x is an int or a float representing a temperature in
                  degrees Fahrenheit.
    """
    return 5*(x-32)/9.0


def to_fahrenheit(x):
    """Returns: x degrees centigrade converted to Fahrenheit

    Precondition: x is an int or a float representing a temperature in
                  centigrade.
    """

    return (x*1.8)+32



def centigrade_to_kelvin(x):

    return x+273.15


def fahrenheit_to_kelvin(x):

    return (x-32)*0.556 + 273.15


def to_kermits(hour, minute, second):

    return ((second)+(minute*60)+(hour*3600))/864
