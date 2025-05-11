#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List


# @lc code=start
class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        occupied_x = set()
        occupied_y = set()
        # diagonal from top_left to bottom-right has the same row - col
        diag_tl = set()
        # diagonal from top_right to bottom-left has the same row + col
        diag_tr = set()

        queens_pos = []

        def chess_board():
            nonlocal queens_pos

            board = [['.'] * n for _ in range(n)]
            for x, y in queens_pos:
                board[x][y] = 'Q'

            return ["".join(row) for row in board]

        def check(x, y):
            nonlocal queens_pos, diag_tl, diag_tr

            # horizontal and vertical check
            # have been checked at generator

            # diagonal check
            if (x - y) in diag_tl or (x + y) in diag_tr:
                return False

            return True

        def add_queen(x, y):
            nonlocal queens_pos, occupied_x, occupied_y, diag_tl, diag_tr
            queens_pos.append((x, y))
            occupied_x.add(x)
            occupied_y.add(y)
            diag_tl.add(x - y)
            diag_tr.add(x + y)

        def remove_queen(x, y):
            nonlocal queens_pos, occupied_x, occupied_y, diag_tl, diag_tr
            queens_pos.pop()
            occupied_x.remove(x)
            occupied_y.remove(y)
            diag_tl.remove(x - y)
            diag_tr.remove(x + y)

        def NQueens_generator(queens_left, row):
            nonlocal queens_pos

            # base case: run out of all queens
            if not queens_left:
                yield chess_board()
                return

            for x in range(row, n):
                # pruning: if rows left is not as many as queens left, this will be a failure case
                if (n - x) < queens_left:
                    break

                for y in range(n):
                    if y in occupied_y:
                        continue

                    if check(x, y):
                        add_queen(x, y)
                        yield from NQueens_generator(queens_left - 1, x + 1)
                        remove_queen(x, y)

        return list(NQueens_generator(n, 0))


# @lc code=end
