"""
A unit test for lab24.py

Authors: Lillian Lee (LJL2) and Walker White (wmw2)
Date:    November 8, 2018
"""

import testcase
import lab24


def test_replace_copy():
    """
    Tests the function replace_copy
    """
    print('Testing replace_copy')
    testcase.assert_equals([4], lab24.replace_copy([5],5,4))
    testcase.assert_equals([], lab24.replace_copy([], 1, 2))
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    testcase.assert_equals([5, 20, 3455, 74, 74, 74, 20], lab24.replace_copy(mylist,3, 20))
    testcase.assert_equals([5, 3, 3455, 74, 74, 74, 3], lab24.replace_copy(mylist, 1, 3))
    print('  replace_copy looks okay')


def test_replace():
    """
    Tests the function replace
    """
    print('Testing replace')
    mylist = [5]
    lab24.replace(mylist,5,4)
    testcase.assert_equals([4], mylist)

    mylist = []
    lab24.replace(mylist,1,2)
    testcase.assert_equals([], mylist)

    mylist = [5, 3, 3455, 74, 74, 74, 3]
    lab24.replace(mylist, 3, 20)
    testcase.assert_equals([5, 20, 3455, 74, 74, 74, 20], mylist)

    lab24.replace(mylist, 1, 3)
    testcase.assert_equals([5, 20, 3455, 74, 74, 74, 20], mylist)
    print('  replace looks okay')


def test_exp():
    """
    Tests the function exp
    """
    print('Testing exp')
    testcase.assert_equals(2.71828,      round(lab24.exp(1),5))
    testcase.assert_equals(2.71828182846,round(lab24.exp(1,1e-12),11))
    testcase.assert_equals(0.13534,      round(lab24.exp(-2),5))
    testcase.assert_equals(0.13533528324,round(lab24.exp(-2,1e-12),11))
    testcase.assert_equals(2981.0,       round(lab24.exp(8,1e-1),0))
    testcase.assert_equals(2980.95799,   round(lab24.exp(8),5))
    testcase.assert_equals(2980.95798704173,round(lab24.exp(8,1e-12),11))
    print('  exp looks okay')


# Script Code
if __name__ == '__main__':
    test_replace_copy()
    test_replace()

    #test_exp()

    print('All tests for lab 24 passed')
