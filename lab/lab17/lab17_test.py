"""
A unit test for Lab 17

Author: Walker M. White (wmw2)
Date:   October 20, 2018
"""
import testcase
import lab17


def test_letter_grades():
    """
    Test procedure for function letter_grades
    """
    print('Testing function letter_grades')
    netids = ['wmw2', 'abc123', 'jms45', 'qoz15', 'xyz2345', 'jms46', 'jms47']
    grades = [ 55,     90,       85,      72,      100,       63,      77    ]
    actual = ['F',    'A',      'B',     'C',     'A',       'D',     'C'    ]

    inputs = dict(zip(netids[:1],grades[:1]))
    result = lab17.letter_grades(inputs)
    testcase.assert_equals(dict(zip(netids[:1],actual[:1])), result)
    testcase.assert_equals(dict(zip(netids[:1],grades[:1])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:3],grades[:3]))
    result = lab17.letter_grades(inputs)
    testcase.assert_equals(dict(zip(netids[:3],actual[:3])), result)
    testcase.assert_equals(dict(zip(netids[:3],grades[:3])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:5],grades[:5]))
    result = lab17.letter_grades(inputs)
    testcase.assert_equals(dict(zip(netids[:5],actual[:5])), result)
    testcase.assert_equals(dict(zip(netids[:5],grades[:5])), inputs)  # Check unmodified

    inputs = dict(zip(netids,grades))
    result = lab17.letter_grades(inputs)
    testcase.assert_equals(dict(zip(netids,actual)), result)
    testcase.assert_equals(dict(zip(netids,grades)), inputs)  # Check unmodified


# Script code
if __name__ == '__main__':
    test_letter_grades()

    print('The function for lab 17 passed all tests')
