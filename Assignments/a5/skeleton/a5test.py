"""Test script for Assigment 5.

This file tests the methods in the class Life, written in the module a5. You
should implement each of these test functions, and keep tweaking your code and
your tests until all of your tests pass.
"""

import a5
import testcase

def test_init():
    """Tests the initializer of Life."""

    # IMPLEMENT ME
    # In the different tests, I am testing the board, width and height of it.
    b1 = a5.Life(4, 5)
    b1_expected = [[".", ".", ".", "."],
                    [".", ".", ".", "."],
                    [".", ".", ".", "."],
                    [".", ".", ".", "."],
                    [".", ".", ".", "."]]
    testcase.assert_equals(b1_expected, b1.board)
    testcase.assert_equals(4, b1.width)
    testcase.assert_equals(5, b1.height)

def test_randomize():
    """Tests the randomize method of Life."""
    # IMPLEMENT ME
    b1 = a5.Life(10, 20)
    b2 = a5.Life(10, 20)

    b1.randomize(1)
    b2.randomize(1)

    testcase.assert_equals(b1.board, b2.board)

    b1 = a5.Life(100, 200)
    b2 = a5.Life(100, 200)

    b1.randomize(10)
    b2.randomize(10)

    testcase.assert_equals(b1.board, b2.board)

    


def test_count_neighbors():
    """Tests the count_neighbors method of Life."""
    # IMPLEMENT ME
    b1 = a5.Life(4, 5)
    b1.board = [[".", "x", ".", "x"],
                [".", "x", "x", "."],
                [".", ".", ".", "."],
                [".", ".", "x", "."],
                [".", ".", ".", "."]]
    
    n1 = b1.count_neighbors(0, 0)
    n2 = b1.count_neighbors(1, 2)

    testcase.assert_equals(n1, 2)
    testcase.assert_equals(n2, 3)


def test_next():
    """Tests the next method of Life."""
    # IMPLEMENT ME
    b1 = a5.Life(4, 5)
    b1.board = [[".", "x", ".", "x"],
                [".", "x", "x", "."],
                [".", ".", ".", "."],
                [".", ".", "x", "."],
                [".", ".", ".", "."]]

    b1.next()
    next1_expected =   [[".", "x", ".", "."],
                        [".", "x", "x", "."],
                        [".", "x", "x", "."],
                        [".", ".", ".", "."],
                        [".", ".", ".", "."]]
    testcase.assert_equals(b1.board, next1_expected)

    b1.next()
    next2_expected =   [[".", "x", "x", "."],
                        ["x", ".", ".", "."],
                        [".", "x", "x", "."],
                        [".", ".", ".", "."],
                        [".", ".", ".", "."]]
    testcase.assert_equals(b1.board, next2_expected)


test_init()
test_randomize()
test_count_neighbors()
test_next()
