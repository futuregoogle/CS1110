"""
Unit test script for Lab 22

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 17, 2019
"""
import testcase
import lab22


def test_numberof():
    """
    Tests for function numberof
    """
    print('Testing numberof')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    testcase.assert_equals(0, lab22.numberof([],4))
    testcase.assert_equals(1, lab22.numberof([4],4))
    testcase.assert_equals(3, lab22.numberof(mylist,74))
    testcase.assert_equals(2, lab22.numberof(mylist,3))
    testcase.assert_equals(0, lab22.numberof(mylist,4))


def test_sum_list():
    """
    Tests for function sum_list
    """
    print('Testing sum_list')
    testcase.assert_equals(0,  lab22.sum_list([]))
    testcase.assert_equals(34, lab22.sum_list([34]))
    testcase.assert_equals(46, lab22.sum_list([7,34,1,2,2]))


# Script Code
if __name__ == '__main__':
    test_numberof()
    test_sum_list()
    print('Module lab22 passed all tests.')
