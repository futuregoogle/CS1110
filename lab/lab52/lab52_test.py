"""
Unit test script for Lab 7

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 17, 2019
"""
import testcase
import lab52


def test_remove_dups():
    """
    Tests for function remove_dups
    """
    print('Testing remove_dups')
    mylist = [1,2,2,3,3,3,4,5,1,1,1]
    testcase.assert_equals([],  lab52.remove_dups([]))
    testcase.assert_equals([3], lab52.remove_dups([3,3]))
    testcase.assert_equals([4], lab52.remove_dups([4]))
    testcase.assert_equals([5], lab52.remove_dups([5, 5]))
    testcase.assert_equals([1,2,3,4,5,1], lab52.remove_dups(mylist))

    # test for whether the code is really returning a copy of the original list
    testcase.assert_equals([1,2,2,3,3,3,4,5,1,1,1], mylist)
    testcase.assert_equals(False, mylist is lab52.remove_dups(mylist))


def test_number_not():
    """
    Tests for function number_not
    """
    print('Testing number_not')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    testcase.assert_equals(0, lab52.number_not([],4))
    testcase.assert_equals(0, lab52.number_not([4],4))
    testcase.assert_equals(4, lab52.number_not(mylist,74))
    testcase.assert_equals(5, lab52.number_not(mylist,3))
    testcase.assert_equals(7, lab52.number_not(mylist,4))


def test_oddsevens():
    """
    Tests for function oddsevens
    """
    mylist = [1,2,3,4,5,6]
    testcase.assert_equals([],     lab52.oddsevens([]))
    testcase.assert_equals([3],    lab52.oddsevens([3]))
    testcase.assert_equals([3,4],  lab52.oddsevens([4,3]))
    testcase.assert_equals([-1,1,2,0],    lab52.oddsevens([-1,0,1,2]))
    testcase.assert_equals([1,3,5,6,4,2], lab52.oddsevens(mylist))

    # test for whether the code is really returning a copy of the original list
    testcase.assert_equals([1,2,3,4,5,6], mylist)
    testcase.assert_equals(False, mylist is lab52.oddsevens(mylist))


def test_remove_first():
    """
    Tests for function remove_first
    """
    print('Testing remove_first')
    testcase.assert_equals([],  lab52.remove_first([],3))
    testcase.assert_equals([],  lab52.remove_first([3],3))
    testcase.assert_equals([3], lab52.remove_first([3],4))
    testcase.assert_equals([3, 4, 4, 5],    lab52.remove_first([3, 4, 4, 4, 5],4))
    testcase.assert_equals([3, 5, 4, 4, 4], lab52.remove_first([3, 4, 5, 4, 4, 4],4))


def test_flatten():
    """
    Tests for function flatten
    """
    print('Testing flatten')
    testcase.assert_equals([],  lab52.flatten([]))
    testcase.assert_equals([3], lab52.flatten([3]))
    testcase.assert_equals([3], lab52.flatten([[3]]))
    testcase.assert_equals([1,2,3,4], lab52.flatten([[1,2],[3,4]]))
    testcase.assert_equals([1,2,3,4,5,6,7], lab52.flatten([[1,[2,3]],[[4,[5,6]],7]]))
    testcase.assert_equals([1,2,3], lab52.flatten([1,2,3]))
    testcase.assert_equals([],  lab52.flatten([[[]],[]]))


def test_sum_to():
    """
    Tests for function sum_to
    """
    print('Testing sum_to')
    testcase.assert_equals(1,  lab52.sum_to(1))
    testcase.assert_equals(6,  lab52.sum_to(3))
    testcase.assert_equals(15, lab52.sum_to(5))


def test_num_digits():
    """
    Tests for function num_digits
    """
    print('Testing num_digits')
    testcase.assert_equals(1, lab52.num_digits(0))
    testcase.assert_equals(1, lab52.num_digits(3))
    testcase.assert_equals(2, lab52.num_digits(34))
    testcase.assert_equals(4, lab52.num_digits(1356))


def test_sum_digits():
    """
    Tests for function sum_digits
    """
    testcase.assert_equals(0,  lab52.sum_digits(0))
    testcase.assert_equals(3,  lab52.sum_digits(3))
    testcase.assert_equals(7,  lab52.sum_digits(34))
    testcase.assert_equals(12, lab52.sum_digits(345))


def test_number2():
    """
    Tests for function number2
    """
    print('Testing number2')
    testcase.assert_equals(0, lab52.number2(0))
    testcase.assert_equals(1, lab52.number2(2))
    testcase.assert_equals(2, lab52.number2(232))
    testcase.assert_equals(0, lab52.number2(333))
    testcase.assert_equals(3, lab52.number2(234252))


def test_into():
    """
    Tests for function into
    """
    print('Testing into')
    testcase.assert_equals(0, lab52.into(5, 3))
    testcase.assert_equals(1, lab52.into(6, 3))
    testcase.assert_equals(2, lab52.into(9, 3))
    testcase.assert_equals(2, lab52.into(18, 3))
    testcase.assert_equals(4, lab52.into(3*3*3*3*7,3))


def test_related():
    """
    Tests for function related
    """
    print('Testing related')
    # GRANDPARENTS
    # John Smith Jr.
    gd1 = person.Person('John','Smith')
    gm1 = person.Person('Jane','Dare')

    gd2 = person.Person('John','Evans')
    gm2 = person.Person('Ellen',"O'Reilly")

    # PARENTS & Uncles
    # John Smith III
    d = person.Person('John','Smith',gm1,gd1)
    m = person.Person('Pamela','Evans',gm2,gd2)
    u = person.Person('Roger','Smith',gm1,gd1)

    # FINAL GENERATION
    # John Smith IV
    p = person.Person('John','Smith',m,d)
    s = person.Person('Ellen','Smith',m,d)
    c = person.Person('Douglas','Smith',None,u)

    testcase.assert_false(lab52.related(p,None))
    testcase.assert_false(lab52.related(None,p))
    testcase.assert_false(lab52.related(None,None))
    testcase.assert_true(lab52.related(p,p))
    testcase.assert_true(lab52.related(p,s))
    testcase.assert_true(lab52.related(p,c))
    testcase.assert_true(lab52.related(d,u))
    testcase.assert_false(lab52.related(m,u))


# Script Code
if __name__ == '__main__':
    test_remove_dups()
    test_number_not()
    test_oddsevens()
    test_flatten()
    test_sum_to()
    test_num_digits()
    test_sum_digits()
    test_number2()
    test_into()
    test_related()
    print('Module lab52 passed all tests.')
