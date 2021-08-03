"""Module to simulate Conway's Game of Life.

This module holds the class Life, which can be used to simulate the board
states in Conway's Game of Life, one generation at a time.

AUTHOR: sp936
"""

import random


class Life:
    """Describes the world of Conway's Game of Life.

    Attribute width: the width of the game world in number of cells.
    Invariant: width is a non-negative integer.

    Attribute height: the height of the game world in number of cells.
    Invariant: height is a non-negative integer.

    Attribute board: the board of the game world.
    Invariant: board is a two-dimensional list of booleans in column-major
    order, of the height and width as specified in the attributes. The value
    True represents a live cell, False represents a dead cell.
    """

    def __init__(self, width, height):
        """Initializes the Game of Life with the given width and height.

        Also initializes the attribute board to be of the right size, and with
        all cells dead.

        Precondition: width and height are nonnegative integers.
        """
        # IMPLEMENT ME
        self.width = width
        self.height = height
        self.board = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(".")
            self.board.append(row)


    def randomize(self, seed_number):
        """Randomizes the current state of the Game of Life with the seed
        number given in the parameter seed_number.

        Precondition: seed_number is an int.
        """
        # IMPLEMENT ME
        random.seed(seed_number)
        for i in range(self.height):
            for j in range(self.width):
                random_number = random.randint(0, 1)
                if random_number == 1:
                    self.board[i][j] = "x"
                else:
                    self.board[i][j] = "."

    def count_neighbors(self, x, y):
        """Counts the number of live neighbors of the cell at (x, y).

        Precondition: x is an int, at least 0 and at most width-1; similarly,
        y is an int, at least 0 and at most height-1.
        """
        # IMPLEMENT ME
        # HINT: You do not have to use a for-loop for this method; just
        # if-statements will suffice. Also, you do not need to indent further
        # than two levels further than this comment.
        neighbours = 0
        if x > 0 and y > 0:
            if self.board[x-1][y-1] == "x":
                neighbours += 1
        if x > 0:
            if self.board[x-1][y] == "x":
                neighbours += 1
        if x > 0 and y < self.width - 1:
            if self.board[x-1][y+1] == "x":
                neighbours += 1
        if y > 0:
            if self.board[x][y-1] == "x":
                neighbours += 1
        if y < self.width - 1:
            if self.board[x][y+1] == "x":
                neighbours += 1
        if x < self.height - 1 and y > 0:
            if self.board[x+1][y-1] == "x":
                neighbours += 1
        if x < self.height - 1:
            if self.board[x+1][y] == "x":
                neighbours += 1
        if x < self.height - 1 and y < self.width - 1:
            if self.board[x+1][y+1] == "x":
                neighbours += 1
        return neighbours

    def next(self):
        """Calculates the next generation and stores it in the attribute board
        of the current instance of Life.

        The rules to calculate the next generation were described in detail in
        the assignment description that you were given.
        """
        # IMPLEMENT ME
        next_board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(".")
            next_board.append(row)

        for i in range(self.height):
            for j in range(self.width):
                neighbours = self.count_neighbors(i, j)
                if self.board[i][j] == 'x':
                    if neighbours == 2 or neighbours == 3:
                        next_board[i][j] = 'x'
                elif neighbours == 3:
                    next_board[i][j] = 'x'

        self.board = next_board

    def print(self):
        """Prints the current state of the board to the output.

        The character 'x' represents a live cell, while the character ' ' (a
        single space!) represents a dead cell.

        Remember the convention we adopted at the beginning of the exercise,
        that told you how the coordinates of the grid were laid out.
        """
        # IMPLEMENT ME
        for i in range(self.height):
            for j in range(self.width):
                print(self.board[i][j], end=" ")
            print()
        print()


if __name__ == "__main__":
    game = Life(5, 5)
    game.randomize(3)
    game.print()
    game.next()
    game.print()
