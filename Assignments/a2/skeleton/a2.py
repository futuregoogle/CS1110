"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: YOUR NETID(S) HERE
Date:   THE DATE COMPLETED HERE
"""


import lab06


# PART A
def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    string1=s.index(' ')
    currency1=s[:string1]
    return currency1


def after_space(string):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space.
    """
    string1=s.index(' ')
    currencytag1=s[string1+1:]
    return currencytag1


# PART B
def get_lhs(json):
    """
    Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a JSON string to parse
    Precondition: json is the response to a currency query
    """
    pass  # PLACEHOLDER. FIRST PUT TEST CASES IN a2test.py, THEN WRITE THE BODY


def get_rhs(json):
    """
    Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "rhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '9916.0137 Euros' (not
    '"9916.0137 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a JSON string to parse
    Precondition: json is the response to a currency query
    """
    pass  # PLACEHOLDER. FIRST PUT TEST CASES IN a2test.py, THEN WRITE THE BODY


def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "ok". For example,
    if the JSON is

    '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Currency amount is invalid').

    Parameter json: a JSON string to parse
    Precondition: json is the response to a currency query
    """
    pass  # PLACEHOLDER. FIRST PUT TEST CASES IN a2test.py, THEN WRITE THE BODY


# PART C
def currency_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the
    currency dst. The response should be a string of the form

    '{ "ok":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "ok" will be followed by the value false (and "err" will have
    an error message).

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string with no spaces or non-letters

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    pass  # PLACEHOLDER. FIRST PUT TEST CASES IN a2test.py, THEN WRITE THE BODY


# PART D
def is_currency(code):
    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """
    pass  # PLACEHOLDER. FIRST PUT TEST CASES IN a2test.py, THEN WRITE THE BODY


def exchange(src, dst, amt):
    """
    Returns the amount received in the given exchange, or -1 in case of error.

    In this exchange, the user is changing amt money in currency src
    to the currency dst. The value returned represents the amount in
    currency dst.

    The value returned has type float.

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    pass  # PLACEHOLDER. FIRST PUT TEST CASES IN a2test.py, THEN WRITE THE BODY
