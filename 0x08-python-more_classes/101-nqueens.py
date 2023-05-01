#!/usr/bin/python3
"""A module that solves the N Queens problem
"""

import sys

class Board:
    """Class Board
    """
    
    def __init__(self, size):
        """the __init__ method initializes the variables
        """
        self.size = size
        self.grid = [[0 for i in range(self.size)] for j in range(self.size)]
        self.solutions = []
        self.find_all_solutions()
        self.print_all_solutions()

    def is_valid(self, row, col):
        """Checking if the board  is valid
        """
        for i in range(col):
            if self.grid[row][i] == 1:
                return False

        # Checking the upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.grid[i][j] == 1:
                return False

        # Checking the lower diagonal on left side
        for i, j in zip(range(row, self.size), range(col, -1, -1)):
            if self.grid[i][j] == 1:
                return False

        return True

    def solve(self, col):
        """the solve method to the nquuens problem
        """
        if col >= self.size:
            solution = []
            for i in range(len(self.grid)):
                for j in range(len(self.grid)):
                    if self.grid[i][j] == 1:
                        solution.append([i, j])
                        break
            self.solutions.append(solution)
            return False

        for i in range(self.size):
            if (self.is_valid(i, col)):
                self.grid[i][col] = 1

                if (self.solve(col + 1)):
                    return True

                self.grid[i][col] = 0
        return False

    def find_all_solutions(self):
        """Finding all the solutions"""
        self.solve(0)

    def print_all_solutions(self):
        """Printing all the solutions
        """
        for solution in self.solutions:
            print(solution)

if __name__ == "__main__":
    """the N Queens problem solution module
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    Board(int(sys.argv[1]))
