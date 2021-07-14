"""
A test script for Lab 15

These unit tests are for the functions in lab15.py.  This script does not do anything
with the asserts.py module.

Author: Walker M. White (wmw2)
Date:   September 25, 2019
"""
import testcase
import lab15


def test_put_in():
    """
    Test procedure for function put_in
    """
    print('Testing function put_in')

    alist = [0,1,2,4]
    result = lab15.put_in(alist,3)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([0,1,2,3,4],alist)

    result = lab15.put_in(alist,-1)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([-1,0,1,2,3,4],alist)

    result = lab15.put_in(alist,2)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([-1,0,1,2,2,3,4],alist)

    result = lab15.put_in(alist,0)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([-1,0,0,1,2,2,3,4],alist)

    alist = []
    result = lab15.put_in(alist,0)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([0],alist)

    result = lab15.put_in(alist,1)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([0,1],alist)


def test_replace_first():
    """
    Test procedure for function replace_first
    """
    print('Testing function replace_first')
    thelist  = [5, 9, 5, 7, 3, 10, 4]
    original = thelist[:]

    # This should return nothing and not modify the list.
    result = lab15.replace_first(thelist,2,8)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals(original,thelist) #If fails, modified the list.

    result = lab15.replace_first(thelist,9,-1)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([5, -1, 5, 7, 3, 10, 4],thelist)

    result = lab15.replace_first(thelist,5,2)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([2, -1, 5, 7, 3, 10, 4],thelist)

    result = lab15.replace_first(thelist,5,2)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([2, -1, 2, 7, 3, 10, 4],thelist)

    result = lab15.replace_first(thelist,5,2)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([2, -1, 2, 7, 3, 10, 4],thelist)

    result = lab15.replace_first(thelist,4,-1)
    testcase.assert_equals(None,result)      #If fails, a value returned
    testcase.assert_equals([2, -1, 2, 7, 3, 10, -1],thelist)


# Script code
if __name__ == '__main__':
    test_put_in()
    test_replace_first()
    print('Module lab15 passed all tests.')
