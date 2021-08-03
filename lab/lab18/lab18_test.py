"""
A unit test for Lab 13

Author: Walker M. White (wmw2)
Date:   October 20, 2018
"""
import testcase
import lab18
import traceback


def test_pair_init():
    """
    Test procedure for the initializer in the Pair class
    """
    print('Testing class Pair (__init__)')

    try:
        lab18.Pair()
    except TypeError:
        pass
    else:
        testcase.quit_with_error('It looks like you have not implemented the initializer yet.')
        exit()

    try:
        result = lab18.Pair(1,2)
    except:
        traceback.print_exc() # Display the stack trace
        testcase.quit_with_error('The constructor call Pair(1,2) crashed.')

    testcase.assert_equals(lab18.Pair, type(result))
    testcase.assert_true(hasattr(result,'first'), 'Class pair has no attribute first')
    testcase.assert_true(hasattr(result,'second'), 'Class pair has no attribute second')
    testcase.assert_equals(1, result.first )
    testcase.assert_equals(2, result.second)

    result = lab18.Pair(3,5)
    testcase.assert_equals(lab18.Pair, type(result))
    testcase.assert_equals(3, result.first )
    testcase.assert_equals(5, result.second)

    for p in [(1, 'foo'), ('foo', 1)]:
        try:
            lab18.Pair(1, 'foo')
        except TypeError:
            pass
        except AssertionError:
            pass
        except BaseException:
            testcase.quit_with_error('The constructor call Pair%s raised an error, but not the right one.' % repr(p))
        else:
            testcase.quit_with_error('The constructor call Pair%s did not enforce its invariant.' % repr(p))


# Script code
if __name__ == '__main__':
    test_pair_init()

    print('The module for lab 18 passed all tests')
