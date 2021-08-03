"""
The for-loop functions for Lab 16.

These functions all require for-loops.

Initial skeleton by W. White (wmw2)

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# IMPLEMENT ALL THIS FUNCTION

def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.

    This function assumes that table has no header, so each row has only
    numbers in it.

    Example: row_sums([[0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [0.5, 1.1, 0.1]])
    returns [0.9, 1.5, 1.7]

    Example: row_sums([[0.2, 0.1], [-0.2, 0.1], [0.2, -0.1], [-0.2, -0.1]])
    returns [0.3, -0.1, 0.1, -0.3]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with no header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) each row contains
    only numbers, and (3) each row is the same length.
    """
        row_sum_list = []   # Empty list to store final row sum


    for row in table:
      row_sum_list.append(round(sum(row), 2))  # Add the sum of row and round to 2 decimal places

    return row_sum_list   # Return the final row sum list
