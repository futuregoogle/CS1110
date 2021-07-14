"""
A unit test for Lab 14

Author: Walker M. White (wmw2)
Date:   October 20, 2018
"""
import testcase
import lab14


def test_lesser_than():
    """
    Test procedure for function lesser_than
    """
    print('Testing function lesser_than')
    thelist = [5, 9, 5, 7, 3, 10, 4]
    testcase.assert_equals(2,lab14.lesser_than(thelist,5))
    testcase.assert_equals(1,lab14.lesser_than(thelist,4))
    testcase.assert_equals(0,lab14.lesser_than(thelist,3))
    testcase.assert_equals(4,lab14.lesser_than(thelist,6))
    testcase.assert_equals(6,lab14.lesser_than(thelist,10))
    testcase.assert_equals(7,lab14.lesser_than(thelist,20))


def test_clamp():
    """
    Test procedure for function clamp
    """
    print('Testing function clamp')

    thelist = [-1, 1, 3, 5]
    result = lab14.clamp(thelist,0,4)
    testcase.assert_equals([0,1,3,4],result)

    thelist = [1, 3]
    result = lab14.clamp(thelist,0,4)
    testcase.assert_equals([1,3],result)

    thelist = [-1, 1, 3, 5]
    result = lab14.clamp(thelist,1,1)
    testcase.assert_equals([1,1,1,1],result)

    thelist = []
    result = lab14.clamp(thelist,0,4)
    testcase.assert_equals([],result)


# Script code
if __name__ == '__main__':
    test_lesser_than()
    test_clamp()

    print('The functions for lab 14 passed all tests')
