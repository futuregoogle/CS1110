"""
Translation support for Pig Latin

This module contains two functions:  first_vowel and pigify. The first is a helper
function of the second (which is the primary function). The second function, pigify,
converts English words to Pig-Latin.  You are to IMPLEMENT the second function.

While you are encouraged to test your answers, you do not need to write  a unit test.
Simply demonstrate your functions to you instructor to get get credit

Author: Walker M. White (wmw2)
Date:   September 21, 2018
"""


def first_vowel(w):
    """
    Returns: position of the first vowel; -1 if no vowels.

    There is a better way to do this function with for-loops,
    but we have not covered that topic yet.

    Parameter w: the word to search
    Precondition: w is a nonempty string with only lowercase letters
    """
    minpos = len(w) # invalid position; currently no vowels found

    # search for a
    pos = w.find('a')
    if pos != -1 and pos < minpos: # a found and is closest
        minpos = pos

    # search for e
    pos = w.find('e')
    if pos != -1 and pos < minpos: # e found and is closest
        minpos = pos

    # search for i
    pos = w.find('i')
    if pos != -1 and pos < minpos: # i found and is closest
        minpos = pos

    # search for o
    pos = w.find('o')
    if pos != -1 and pos < minpos: # o found and is closest
        minpos = pos

    # search for u
    pos = w.find('u')
    if pos != -1 and pos < minpos: # u found and is closest
        minpos = pos

    # search for y not at front
    backpos = w[1:].find('y')
    if backpos != -1: # y found in "back part"
        pos = backpos + 1; # position of y in w
        if pos < minpos: # y found in w and is closest
            minpos = pos

    # found something if minpos moved from first assignment
    return minpos if minpos != len(w) else -1


def pigify(w):
    """
    Returns: copy of w converted to Pig Latin

    See the lab handout for the complete rules on Pig Latin.

    Parameter w: the word to change to Pig Latin
    Precondition: w is a nonempty string with only lowercase letters
    """

    assert w.isalpha()
    assert w.islower()

    if first_vowel(w) == 0:
        w = w + 'hay'
    elif w[0] == 'q':
        if w[1] == 'u':
            w = w[2:] + 'quay'
    else:
        for _ in range(len(w)):
            if first_vowel(w) == 0: break
            else:
                w = w[1:] + w[0]
        w = w + 'ay'

    print(w)
