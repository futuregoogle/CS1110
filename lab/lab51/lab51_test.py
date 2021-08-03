"""
A unit test for Lab 51

Author: Walker M. White (wmw2)
Date:   October 20, 2018
"""
import testcase
import lab51
import copy


def test_uniques():
    """
    Test procedure for function uniques
    """
    print('Testing function uniques')
    thelist = [5, 9, 5, 7] 
    testcase.assert_equals(3,lab51.uniques(thelist))
    
    thelist = [5, 5, 1, 'a', 5, 'a']
    testcase.assert_equals(3,lab51.uniques(thelist))
    
    thelist = [1, 2, 3, 4, 5]
    testcase.assert_equals(5,lab51.uniques(thelist))
    
    thelist = []
    testcase.assert_equals(0,lab51.uniques(thelist))
    
    # Make sure the function does not modify the original
    thelist = [5, 9, 5, 7]
    result  = lab51.uniques(thelist)
    testcase.assert_equals([5, 9, 5, 7],thelist)


def test_removeall():
    """
    Test procedure for removeall
    """
    print('Testing function removeall')
    
    alist = [1,2,2,3,1]
    result = lab51.removeall(alist,1)
    testcase.assert_equals([2,2,3],result)
    testcase.assert_equals([1,2,2,3,1],alist)
    
    result = lab51.removeall(alist,2)
    testcase.assert_equals([1,3,1],result)
    testcase.assert_equals([1,2,2,3,1],alist)
    
    result = lab51.removeall(alist,5)
    testcase.assert_equals([1,2,2,3,1],result)
    testcase.assert_equals([1,2,2,3,1],alist)
    
    alist = [3,3,3]
    result = lab51.removeall(alist,3)
    testcase.assert_equals([],result)
    testcase.assert_equals([3,3,3],alist)
    
    alist = [3,3,3]
    result = lab51.removeall(alist,1)
    testcase.assert_equals([3,3,3],result)
    testcase.assert_equals([3,3,3],alist)
    
    alist = [7]
    result = lab51.removeall(alist,7)
    testcase.assert_equals([],result)
    testcase.assert_equals([7],alist)
    
    alist = []
    result = lab51.removeall(alist,7)
    testcase.assert_equals([],result)
    testcase.assert_equals([],alist)


def test_place_sums():
    """
    Test procedure for function place_sums
    
    Note the use of assert_float_lists_equal for testing (nested) lists
    of floats.
    """
    print('Testing function place_sums')
    
    table = [['I1','I2','I3'], [0.8, 0.2], [0.6, 0.9], [0.4, 0.3]]
    goal  = [['I1','I2','I3','Sum'], [0.8, 0.2, 1.0], [0.6, 0.9, 1.5], [0.4, 0.3, 0.7]]
    lab51.place_sums(table)
    testcase.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        testcase.assert_float_lists_equal(goal[pos],table[pos])
    
    table = [['I1','I2'], [0.2, -0.6, 0.1], [0.9, 0.8, -1.0]]
    goal  = [['I1','I2','Sum'], [0.2, -0.6, 0.1, -0.3], [0.9, 0.8, -1.0, 0.7]]
    lab51.place_sums(table)
    testcase.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        testcase.assert_float_lists_equal(goal[pos],table[pos])
    
    table = [['I1'], [0.4, 0.8, 0.5, 0.4]]
    goal  = [['I1','Sum'], [0.4, 0.8, 0.5, 0.4, 2.1]]
    lab51.place_sums(table)
    testcase.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        testcase.assert_float_lists_equal(goal[pos],table[pos])
    
    table = [['I1','I2','I3','I4'], [0.3], [0.5], [0.8], [0.4]]
    goal  = [['I1','I2','I3','I4','Sum'], [0.3, 0.3], [0.5, 0.5], [0.8, 0.8], [0.4, 0.4]]
    lab51.place_sums(table)
    testcase.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        testcase.assert_float_lists_equal(goal[pos],table[pos])


def test_crossout():
    """
    Test procedure for function crossout.
    
    Note the use of assert_float_lists_equal for testing (nested) lists
    of floats.
    """
    print('Testing function crossout')
    
    table = [[0.1,0.3,0.5],[0.6,0.2,0.7],[1.5,2.3,0.4]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = lab51.crossout(table,1,2)
    testcase.assert_float_lists_equal([[0.1,0.3],[1.5,2.3]],result)
    testcase.assert_float_lists_equal(orig,table)
    
    result = lab51.crossout(table,0,0)
    testcase.assert_float_lists_equal([[0.2,0.7],[2.3,0.4]],result)
    testcase.assert_float_lists_equal(orig,table)
   
    result = lab51.crossout(table,2,1)
    testcase.assert_float_lists_equal([[0.1,0.5],[0.6,0.7]],result)
    testcase.assert_float_lists_equal(orig,table)
    
    table = [[0.1,0.3,0.5],[0.6,0.2,0.7],[1.5,2.3,0.4],[0.1,0.2,0.3]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = lab51.crossout(table,1,2)
    testcase.assert_float_lists_equal([[0.1,0.3],[1.5,2.3],[0.1,0.2]],result)
    testcase.assert_float_lists_equal(orig,table)
    
    table = [[0.1,0.3,0.5,1.0],[0.6,0.2,0.7,2.0],[1.5,2.3,0.4,3.0]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = lab51.crossout(table,1,2)
    testcase.assert_float_lists_equal([[0.1,0.3,1.0],[1.5,2.3,3.0]],result)
    testcase.assert_float_lists_equal(orig,table)
    
    table = [[1,2],[3,4]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = lab51.crossout(table,1,0)
    testcase.assert_float_lists_equal([[2]],result)
    testcase.assert_float_lists_equal(orig,table)
    
    result = lab51.crossout(table,0,1)
    testcase.assert_float_lists_equal([[3]],result)
    testcase.assert_float_lists_equal(orig,table)
    
    table = [[5]]
    # Snapshot table to make sure we do not modify
    orig = copy.deepcopy(table)
    result = lab51.crossout(table,0,0)
    testcase.assert_equals([],result)
    testcase.assert_float_lists_equal(orig,table)


def test_average_grade():
    """
    Test procedure for function average_grade
    """
    print('Testing function average_grade')
    netids = ['wmw2', 'abc123', 'jms45', 'qoz15', 'xyz2345', 'jms46', 'jms47']
    grades = [ 55,     90,       85,      72,      100,       63,      77    ]
    
    inputs = dict(zip(netids[:1],grades[:1]))
    result = lab51.average_grade(inputs)
    testcase.assert_floats_equal(55.0,result)
    testcase.assert_equals(dict(zip(netids[:1],grades[:1])), inputs)  # Check unmodified
    
    inputs = dict(zip(netids[:3],grades[:3]))
    result = lab51.average_grade(inputs)
    testcase.assert_floats_equal(76.666666667,result)
    testcase.assert_equals(dict(zip(netids[:3],grades[:3])), inputs)  # Check unmodified
    
    inputs = dict(zip(netids[:5],grades[:5]))
    result = lab51.average_grade(inputs)
    testcase.assert_floats_equal(80.4,result)
    testcase.assert_equals(dict(zip(netids[:5],grades[:5])), inputs)  # Check unmodified
    
    inputs = dict(zip(netids,grades))
    result = lab51.average_grade(inputs)
    testcase.assert_floats_equal(77.428571428,result)
    testcase.assert_equals(dict(zip(netids,grades)), inputs)  # Check unmodified


def test_convert_grades():
    """
    Test procedure for function convert_grades.
    """
    print('Testing function convert_grades')
    
    grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
    answer = {'wmw2': 'F', 'abc3': 'A', 'jms45': 'B'}
    result = lab51.convert_grades(grades)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = {'abc123': 0,'abc456':65,'jms457':50}
    answer = {'abc123': 'F','abc456':'D','jms457':'F'}
    result = lab51.convert_grades(grades)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D','xyz123':'C'}
    result = lab51.convert_grades(grades)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,'xyz456':80,'wmw4':90}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D','xyz123':'C','xyz456':'B','wmw4':'A'}
    result = lab51.convert_grades(grades)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
              'xyz456':80,'wmw4':90,'wmw5':100}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D',
              'xyz123':'C','xyz456':'B','wmw4':'A','wmw5':'A'}
    result = lab51.convert_grades(grades)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
              'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}
    answer = {'abc123': 'F','abc456':'D','jms457':'F','jms123':'D',
              'xyz123':'C','xyz456':'B','wmw4':'A','wmw5':'A','tor3':'B'}
    result = lab51.convert_grades(grades)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = {'wmw2' : 55, 'abc3' : 90}
    answer = {'wmw2' : 'F', 'abc3' : 'A'}
    result = lab51.convert_grades(grades)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = {'abc3' : 90}
    answer = {'abc3' : 'A'}
    result = lab51.convert_grades(grades)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = {}
    answer = {}
    result = lab51.convert_grades(grades)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)


def test_drop_below():
    """
    Test procedure for function drop_below.
    """
    print('Testing function drop_below')
    
    orignl = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
    grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
    answer = {'abc3': 90, 'jms45': 86}
    result = lab51.drop_below(grades,20)
    testcase.assert_equals(None,result)
    testcase.assert_equals(orignl,grades)
    
    result = lab51.drop_below(grades,55)
    testcase.assert_equals(None,result)
    testcase.assert_equals(orignl,grades)
    
    result = lab51.drop_below(grades,60)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = copy.deepcopy(orignl)
    result = lab51.drop_below(grades,86)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    grades = copy.deepcopy(orignl)
    result = lab51.drop_below(grades,95)
    testcase.assert_equals(None,result)
    testcase.assert_equals({},grades)
    
    orignl = {'abc123': 0,'abc456':65,'jms457':50,'jms123':60,'xyz123':70,
              'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}
    grades = copy.deepcopy(orignl)
    answer = {'xyz456':80,'wmw4':90,'wmw5':100,'tor3':88}
    
    result = lab51.drop_below(grades,0)
    testcase.assert_equals(None,result)
    testcase.assert_equals(orignl,grades)
    
    result = lab51.drop_below(grades,80)
    testcase.assert_equals(None,result)
    testcase.assert_equals(answer,grades)
    
    orignl = {'abc3' : 90}
    grades = {'abc3' : 90}
    result = lab51.drop_below(grades,90)
    testcase.assert_equals(None,result)
    testcase.assert_equals(orignl,grades)
    
    result = lab51.drop_below(grades,100)
    testcase.assert_equals(None,result)
    testcase.assert_equals({},grades)
    
    grades = {}
    result = lab51.drop_below(grades,0)
    testcase.assert_equals(None,result)
    testcase.assert_equals({},grades)


# Script code
if __name__ == '__main__':
    test_uniques()
    test_removeall()
    test_place_sums()
    test_crossout()
    test_average_grade()
    test_convert_grades()
    test_drop_below()
    print('The modules for lab 51 passed all tests')
