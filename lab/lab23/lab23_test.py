"""
Unit test script for Lab 7

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 17, 2019
"""
import testcase
import lab23


def test_replace():
    """
    Tests for function replace
    """
    print('Testing replace')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    testcase.assert_equals([],  lab23.replace([], 1, 2))
    testcase.assert_equals([4], lab23.replace([5],5,4))
    testcase.assert_equals([5, 20, 3455, 74, 74, 74, 20], lab23.replace(mylist,3, 20))
    testcase.assert_equals([5, 3, 3455, 74, 74, 74, 3],   lab23.replace(mylist, 1, 3))

    # test for whether the code is really returning a copy of the original list
    testcase.assert_equals([5, 3, 3455, 74, 74, 74, 3], mylist)
    testcase.assert_equals(False, mylist is lab23.replace(mylist, 1, 3))


def test_remove_first():
    """
    Tests for function remove_first
    """
    print('Testing remove_first')
    testcase.assert_equals([],  lab23.remove_first([],3))
    testcase.assert_equals([],  lab23.remove_first([3],3))
    testcase.assert_equals([3], lab23.remove_first([3],4))
    testcase.assert_equals([3, 4, 4, 5],    lab23.remove_first([3, 4, 4, 4, 5],4))
    testcase.assert_equals([3, 5, 4, 4, 4], lab23.remove_first([3, 4, 5, 4, 4, 4],4))


# Script Code
if __name__ == '__main__':
    test_replace()
    test_remove_first()
    print('Module lab23 passed all tests.')
