"""
A test script to test the module func.py

AUTHOR: YOUR NETID HERE
DATE: DATE COMPLETED HERE
"""

import testcase      # For assert_equals, assert_floats_equal, and assert_true
import funcs         # This is what we are testing


# PART 1
print('Testing the testcase asserts')
testcase.assert_equals('b c', 'ab cd'[1:4])
#testcase.assert_equals('b c', 'ab cd'[1:3])     # UNCOMMENT ONLY WHEN DIRECTED

testcase.assert_true(3 < 4)
testcase.assert_equals(3, 1+2)

testcase.assert_equals(3.0, 1.0+2.0)
testcase.assert_floats_equal(6.3, 3.1+3.2)
#testcase.assert_equals(6.3, 3.1+3.2)            # UNCOMMENT ONLY WHEN DIRECTED


# PART 2 GOES HERE
print(testcase.assert_equals(True, funcs.has_a_vowel('aeiou')))

# INDICATES THAT EVERYTHING WORKS
print('Module funcs is working correctly')
