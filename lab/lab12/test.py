"""
A test script for lab12

Run this test script to make sure everything is working properly.

Author: Walker White (wmw2)
Date:   November 2, 2018
"""
import testcase
import lab12


def test_get_previous():
    """
    Tests the get_previous function
    """
    print('Testing the function get_previous')

    testcase.assert_equals(22,   lab12.get_previous('file_good.txt'))
    testcase.assert_equals('ABC',lab12.get_previous('file_bad.txt'))
    testcase.assert_equals(None, lab12.get_previous('file_huh.txt'))

    fail = False
    try:
        lab12.get_previous(12)
        fail = True
    except AssertionError:
        pass
    except:
        testcase.quit_with_error('Function get_previous is not enforcing preconditions.')

    if fail:
        testcase.quit_with_error('Function get_previous is not enforcing preconditions.')


def test_divide_even():
    """
    Tests the divide_even function
    """
    print('Testing the function divide_even')

    testcase.assert_error(lab12.divide_even, 'bla', error=TypeError, reason='number should be an int')
    testcase.assert_error(lab12.divide_even, 31, error=ValueError, reason='number should be even')
    testcase.assert_equals(int, type(lab12.divide_even(32)))
    testcase.assert_equals(16, lab12.divide_even(32))


# Script code
if __name__ == '__main__':
    test_get_previous()
    test_divide_even()

    print('The module lab12 passed all tests')
