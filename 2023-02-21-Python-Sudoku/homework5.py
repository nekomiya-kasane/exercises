############################################################
# CIS 5210: Homework 5
############################################################

# Include your imports here, if any are used.

import collections
import copy
import itertools
import random
import math

student_name = "Type your full name here."

############################################################
# Sudoku Solver
############################################################


def sudoku_cells():
    return [(i, j) for i in range(9) for j in range(9)]


def sudoku_arcs():
    row_arcs = {((i, j), (i, k))
                for j in range(9)
                for k in range(9) if j != k
                for i in range(9)
                }
    col_arcs = {((j, i), (k, i))
                for j in range(9)
                for k in range(9) if j != k
                for i in range(9)
                }
    block_arcs = list(filter(
        lambda x: x[0][0] != x[1][0] and x[0][1] != x[1][1],
        [((i, j), (k, m))
         for i in range(3)
         for j in range(3)
         for k in range(3)
         for m in range(3)
         ]))
    multi_block_arcs = {
        ((x[0][0] + 3 * i, x[0][1] + 3 * j),
         (x[1][0] + 3 * i, x[1][1] + 3 * j))
        for x in block_arcs for i in range(3) for j in range(3)
    }
    return row_arcs | col_arcs | multi_block_arcs


def read_board(path):
    res = collections.defaultdict(set)
    with open(path, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        for i in range(9):
            for j in range(9):
                res[(i, j)] = {i for i in range(1, 10)} \
                    if lines[i][j] == '*' else {int(lines[i][j])}
    return res


class Sudoku(object):

    CELLS: list[tuple[int, int]] = sudoku_cells()
    ARCS: set[tuple[tuple[int, int], tuple[int, int]]] = sudoku_arcs()

    board: dict[tuple[int, int], set[int]] = {}

    def __init__(self, board: dict[tuple[int, int], set[int]]):
        self.board = board

    def get_values(self, cell: tuple[int, int]) -> set[int]:
        return self.board[cell]

    def remove_inconsistent_values(self,
                                   cell1: tuple[int, int],
                                   cell2: tuple[int, int]):
        removed = set()

        if (cell1, cell2) in self.ARCS and len(self.board[cell2]) == 1:
            removed |= self.board[cell2]
        new = self.board[cell1] - removed

        changed = bool(len(self.board[cell1]) - len(new))

        self.board[cell1] = new
        return changed

    def infer_ac3(self):
        qu = collections.deque(self.ARCS)
        while qu:
            fm, to = qu.pop()
            # find upstream
            if len(self.board[fm]) > 1 and \
                    self.remove_inconsistent_values(fm, to):
                for arc in self.ARCS:
                    if arc[0] == fm or arc[1] == fm and arc != (fm, to):
                        qu.append(arc)

    def uniquifiable(self, cell, value) -> bool:
        # unique in block (row, col excepted)
        def check_block() -> bool:
            R = cell[0] // 3
            C = cell[1] // 3
            for i in range(3 * R, 3 * R + 3):
                for j in range(3 * C, 3 * C + 3):
                    if (i, j) == cell:
                        continue
                    if value in self.board[(i, j)]:
                        return False
            return True

        if check_block():
            return True

        # rows
        def check_row() -> bool:
            for j in range(9):
                if j == cell[1]:
                    continue
                if value in self.board[(cell[0], j)]:
                    return False
            return True

        if check_row():
            return True

        # columns
        def check_col() -> bool:
            for i in range(9):
                if i == cell[0]:
                    continue
                if value in self.board[(i, cell[1])]:
                    return False
            return True

        return check_col()

    def infer_improved(self):
        renew = True
        while renew:
            self.infer_ac3()
            renew = False
            for cell in self.CELLS:
                if len(self.board[cell]) <= 1:
                    continue
                for i in self.board[cell]:
                    if not self.uniquifiable(cell, i):
                        continue
                    self.board[cell] = {i}
                    renew = True  # new information provided
                    break

    def check_valid(self) -> bool:
        for fm, to in self.ARCS:
            if len(self.board[fm] | self.board[to]) <= 1:
                return False
        return True

    def infer_with_guessing(self):
        self.infer_improved()

        for cell in self.CELLS:
            if len(self.board[cell]) == 1:
                continue

            this_board = self.board.copy()

            for i in self.board[cell]:
                self.board[cell] = {i}
                res = self.infer_with_guessing()

                if not res:
                    self.board = this_board
                else:
                    return True
            return False

        return self.check_valid()


############################################################
# Feedback
############################################################


# Just an approximation is fine.
feedback_question_1 = 2.5

feedback_question_2 = """
It's challenging to consider all possible situations and correctly
manipulate the indices and values.
Also, as there're so many possibilities, it's also challenging to
optimize the process and reduce memory 
costs.
There's no special stumbling blocks for me, but debugging really
takes a long time.
"""

feedback_question_3 = """
The AC-3 algorithm to handle finite valued constrained system is great,
I think I can also apply this algorithm to my graph constraints solver.
"""
