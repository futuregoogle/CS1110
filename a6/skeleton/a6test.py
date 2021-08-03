"""Test script for Assigment 6.

This file tests the functions you wrote in the module a6.

AUTHOR: sp936
"""

import a6
import testcase
import math


def test_binary_search():
    """Tests the function binary_search."""
    # IMPLEMENT ME
    l1 = [0, 2, 5, 8, 10, 42, 101]
    n1 = 101

    l2 = [2, 3, 5, 7, 11, 13, 17, 19]
    n2 = 9

    l3 = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    n3 = 1

    l4 = [0, 0, 5, 28, 9001]
    n4 = 91

    testcase.assert_equals(True, a6.binary_search(l1, n1))
    testcase.assert_equals(False, a6.binary_search(l2, n2))
    testcase.assert_equals(True, a6.binary_search(l3, n3))
    testcase.assert_equals(False, a6.binary_search(l4, n4))


def test_revert():
    """Tests the function revert."""
    # IMPLEMENT ME
    l1 = [1, 2, 3, 4, 5]
    l2 = ['A', 'man', 'a', 'plan', 'a', 'canal', 'Panama']
    l3 = ['Sator', 'Arepo', 'Tenet', 'Opera', 'Rotas']

    testcase.assert_equals(l1[::-1], a6.revert(l1))
    testcase.assert_equals(l2[::-1], a6.revert(l2))
    testcase.assert_equals(l3[::-1], a6.revert(l3))


def test_gray_code():
    """Tests the function gray_code."""
    # IMPLEMENT ME
    g0 = [[]]
    g1 = [[True], [False]]
    g2 = [[False, False], [False, True], [True, True], [True, False]]
    g3 = [[False, False, False],
        [False, False, True],
        [False, True, True],
        [False, True, False],
        [True, True, False],
        [True, True, True],
        [True, False, True],
        [True, False, False]]

    testcase.assert_equals(g0, a6.gray_code(0))
    testcase.assert_equals(g1, a6.gray_code(1))
    testcase.assert_equals(g2, a6.gray_code(2))
    testcase.assert_equals(g3, a6.gray_code(3))


def test_approx_sqrt():
    """Tests the function approx_sqrt."""
    # IMPLEMENT ME
    n1 = 2
    n2 = 104
    n3 = 909172
    n4 = 9102937291

    testcase.assert_floats_equal(math.sqrt(n1), a6.approx_sqrt(n1, 0.001))
    testcase.assert_floats_equal(math.sqrt(n2), a6.approx_sqrt(n2, 0.001))
    testcase.assert_floats_equal(math.sqrt(n3), a6.approx_sqrt(n3, 0.001))
    testcase.assert_floats_equal(math.sqrt(n4), a6.approx_sqrt(n4, 0.001))
