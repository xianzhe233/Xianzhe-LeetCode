#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
from math import sqrt
from typing import List


# @lc code=start
class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        SIZE = 9
        SIDE_LENGTH = int(sqrt(SIZE))
        NUMS = tuple(range(1, 10))

        row_nums: list[set[int]] = [set() for _ in range(SIZE)]
        col_nums: list[set[int]] = [set() for _ in range(SIZE)]
        sub_nums: list[list[set[int]]] = [
            [set() for _ in range(SIDE_LENGTH)] for _ in range(SIDE_LENGTH)
        ]
        empty_cells = [(x, y)
                       for x in range(SIZE)
                       for y in range(SIZE)
                       if board[x][y] == '.']

        def sub_box(row, col):
            return row // 3, col // 3

        # initialize sets
        for i in range(SIZE):
            for j in range(SIZE):
                char = board[i][j]
                if char == '.':
                    continue
                num = int(char)
                row_nums[i].add(num)
                col_nums[j].add(num)
                sub_row, sub_col = sub_box(i, j)
                sub_nums[sub_row][sub_col].add(num)

        def check(row, col, num):
            if num in row_nums[row] or num in col_nums[col]:
                return False
            sub_row, sub_col = sub_box(row, col)
            return num not in sub_nums[sub_row][sub_col]

        def add_number(row, col, num):
            board[row][col] = str(num)
            row_nums[row].add(num)
            col_nums[col].add(num)
            sub_row, sub_col = sub_box(row, col)
            sub_nums[sub_row][sub_col].add(num)

        def remove_number(row, col, num):
            board[row][col] = '.'
            row_nums[row].remove(num)
            col_nums[col].remove(num)
            sub_row, sub_col = sub_box(row, col)
            sub_nums[sub_row][sub_col].remove(num)

        def solver(empty_cell_index):
            nonlocal board, empty_cells, row_nums, col_nums, sub_nums

            # base case: fill all empty cells successfully
            if empty_cell_index == len(empty_cells):
                return True

            # coordinates of current empty cell
            x, y = empty_cells[empty_cell_index]
            for num in NUMS:
                if check(x, y, num):
                    add_number(x, y, num)
                    if solver(empty_cell_index + 1):
                        # a valid solution has been found
                        return True
                    else:
                        remove_number(x, y, num)

            # No valid solution with previous settings
            return False

        solver(0)
        return


# @lc code=end
