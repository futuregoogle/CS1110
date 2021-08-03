"""
A unit test for Lab 16

Author: Walker M. White (wmw2)
Date:   October 20, 2018
"""
import testcase
import lab16


def test_row_sums():
    """
    Test procedure for function row_sums

    Note the use of assert_float_lists_equal for testing (nested) lists
    of floats.
    """
    print('Testing function row_sums')
    result = lab16.row_sums([[0.8, 0.2], [0.6, 0.9], [0.4, 0.3]])
    testcase.assert_float_lists_equal([1.0, 1.5, 0.7],result)
    result = lab16.row_sums([[0.2, -0.6, 0.1], [0.9, 0.8, -1.0]])
    testcase.assert_float_lists_equal([-0.3, 0.7],result)
    result = lab16.row_sums([[0.4, 0.8, 0.5, 0.4]])
    testcase.assert_float_lists_equal([2.1],result)
    result = lab16.row_sums([[0.3], [0.5], [0.8], [0.4]])
    testcase.assert_float_lists_equal([0.3, 0.5, 0.8, 0.4],result)


# Script code
if __name__ == '__main__':
    test_row_sums()

    print('The function for lab 16 passed all tests')
