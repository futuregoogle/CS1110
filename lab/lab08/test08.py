"""
A unit test for Lab 08

Author: Walker M. White (wmw2)
Date:   September 20, 2018
"""
import testcase
import lab08
from timer import Time


def test_add_time():
    """
    Test procedure for function add_time
    """
    print('Testing function add_time')

    time1 = Time(2,15)
    time2 = Time(3,30)
    result = lab08.add_time(time1,time2)

    testcase.assert_equals(Time,type(result))
    testcase.assert_equals(5,result.hours)
    testcase.assert_equals(45,result.minutes)
    # Make sure you did not modify the original times
    testcase.assert_equals(2, time1.hours)
    testcase.assert_equals(15,time1.minutes)
    testcase.assert_equals(3, time2.hours)
    testcase.assert_equals(30,time2.minutes)

    time1 = Time(15,35)
    time2 = Time(10,45)
    result = lab08.add_time(time1,time2)

    testcase.assert_equals(Time,type(result))
    testcase.assert_equals(26,result.hours)
    testcase.assert_equals(20,result.minutes)
    # Make sure you did not modify the original times
    testcase.assert_equals(15,time1.hours)
    testcase.assert_equals(35,time1.minutes)
    testcase.assert_equals(10,time2.hours)
    testcase.assert_equals(45,time2.minutes)

    time1 = Time(0,5)
    time2 = Time(3,55)
    result = lab08.add_time(time1,time2)

    testcase.assert_equals(Time,type(result))
    testcase.assert_equals(4,result.hours)
    testcase.assert_equals(0,result.minutes)
    # Make sure you did not modify the original times
    testcase.assert_equals(0,time1.hours)
    testcase.assert_equals(5,time1.minutes)
    testcase.assert_equals(3,time2.hours)
    testcase.assert_equals(55,time2.minutes)

# Script code
if __name__ == '__main__':
    test_add_time()
    print('Lab 8 is working correctly')
